#!/usr/bin/env python3
"""Unit 04-05：7B vLLM 识图与「识图反复」0-1000 归一化坐标闭环模板。"""
from __future__ import annotations

import base64
import json
import re
import urllib.request
from pathlib import Path

_DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def ask_vlm(endpoint: str, model: str, image_path: Path, prompt: str, api_key: str = "EMPTY") -> str:
    b64 = base64.b64encode(image_path.read_bytes()).decode("ascii")
    payload = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                {"type": "text", "text": prompt},
            ],
        }],
        "max_tokens": 180,
        "temperature": 0.0,
    }
    req = urllib.request.Request(
        f"{endpoint.rstrip('/')}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    with _DIRECT.open(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))["choices"][0]["message"]["content"].strip()


def visual_retry_loop(capture_fn, act_fn, endpoint: str, model: str, target: str, max_rounds: int = 3) -> bool:
    """截图 -> VLM 0-1000 定位 -> 执行动作 -> 再截图复检，直到 PASS。"""
    for round_idx in range(1, max_rounds + 1):
        img = Path(capture_fn(round_idx))
        coord_raw = ask_vlm(
            endpoint, model, img,
            f"Locate 【{target}】 in 0-1000 normalized coordinates. Output JSON ONLY: {{\"x\": int, \"y\": int}}",
        )
        m = re.search(r"\{[^}]+\}", coord_raw)
        if not m:
            continue
        pt = json.loads(m.group(0))
        act_fn(int(pt["x"]), int(pt["y"]))
        verify_img = Path(capture_fn(f"{round_idx}_verify"))
        verdict = ask_vlm(endpoint, model, verify_img, f"确认操作【{target}】是否已生效且界面无遮挡？只答 PASS 或 FAIL 并简述。")
        if "PASS" in verdict.upper() and "FAIL" not in verdict.upper():
            return True
    return False
