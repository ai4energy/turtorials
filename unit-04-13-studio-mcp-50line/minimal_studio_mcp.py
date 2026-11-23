#!/usr/bin/env python3
"""Unit 04-13：50 行极简 Studio MCP Server 教学蓝图（对比 L3 网页与 L4 AI 工具调用）。"""
from __future__ import annotations

import json
from pathlib import Path


def tool_tts_clone(text: str, out_wav: str = "sample.wav") -> dict:
    return {"ok": True, "tool": "tts_clone", "out_wav": out_wav, "chars": len(text)}


def tool_ffmpeg_weld(video: str, audio: str, out_mp4: str = "sample_10s.mp4") -> dict:
    return {"ok": True, "tool": "ffmpeg_weld", "out_mp4": out_mp4, "inputs": [video, audio]}


def tool_qa_gate(report_json: str) -> dict:
    p = Path(report_json)
    data = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"all_passed": True}
    return {"ok": bool(data.get("all_passed", False)), "tool": "qa_gate"}


TOOLS = {
    "tts_clone": tool_tts_clone,
    "ffmpeg_weld": tool_ffmpeg_weld,
    "qa_gate": tool_qa_gate,
}

if __name__ == "__main__":
    # 极简 stdio JSON-RPC / CLI 自测示例（无额外重依赖，也可无缝接 FastMCP）
    print(json.dumps({
        "registered_tools": list(TOOLS.keys()),
        "demo_tts": TOOLS["tts_clone"]("十秒样片自动配音"),
        "demo_weld": TOOLS["ffmpeg_weld"]("manim.mp4", "sample.wav"),
    }, ensure_ascii=False, indent=2))
