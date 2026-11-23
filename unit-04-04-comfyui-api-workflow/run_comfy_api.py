#!/usr/bin/env python3
"""Unit 04-04：ComfyUI API JSON 提交、轮询队列与 POST /free 显存回收最小示例。"""
from __future__ import annotations

import argparse
import json
import time
import urllib.request
from pathlib import Path

_DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def post_json(url: str, payload: dict) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with _DIRECT.open(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8") or "{}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:18130")
    ap.add_argument("--workflow", default="workflow_api.json")
    ap.add_argument("--free-after", action="store_true")
    args = ap.parse_args()

    wf = json.loads(Path(args.workflow).read_text(encoding="utf-8"))
    res = post_json(f"{args.url.rstrip('/')}/prompt", {"prompt": wf})
    pid = res.get("prompt_id")
    print("Submitted prompt_id:", pid)

    for _ in range(60):
        with _DIRECT.open(f"{args.url.rstrip('/')}/history/{pid}", timeout=10) as r:
            hist = json.loads(r.read().decode("utf-8"))
        if pid in hist:
            print("Completed outputs:", list(hist[pid].get("outputs", {}).keys()))
            break
        time.sleep(1.0)

    if args.free_after:
        post_json(f"{args.url.rstrip('/')}/free", {"unload_models": True, "free_memory": True})
        print("VRAM freed via POST /free")


if __name__ == "__main__":
    main()
