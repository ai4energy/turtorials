#!/usr/bin/env python3
"""Unit 04-07：ffmpeg 五大焊法封装 + vncdotool 桌面自动点击录屏最小示范。"""
from __future__ import annotations

import subprocess
from pathlib import Path


def loudnorm_16lufs(src_wav: Path, dst_wav: Path) -> None:
    subprocess.run(
        [
            "ffmpeg", "-v", "error", "-y", "-i", str(src_wav),
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(dst_wav),
        ],
        check=True,
    )


def overlay_timed_layer(base_mp4: Path, overlay_png: Path, out_mp4: Path, t0: float, t1: float) -> None:
    subprocess.run(
        [
            "ffmpeg", "-v", "error", "-y", "-i", str(base_mp4),
            "-loop", "1", "-i", str(overlay_png),
            "-filter_complex", f"[0:v][1:v]overlay=0:0:enable='between(t,{t0:.3f},{t1:.3f})':shortest=1[v]",
            "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "copy", str(out_mp4),
        ],
        check=True,
    )


def vnc_click_and_type(server: str, x: int, y: int, text: str, shot_out: Path) -> None:
    from vncdotool import api
    client = api.connect(server, password=None)
    try:
        client.mouseMove(x, y)
        client.mousePress(1)
        for ch in text:
            client.keyPress("space" if ch == " " else ch)
        client.captureScreen(str(shot_out))
    finally:
        client.disconnect()
