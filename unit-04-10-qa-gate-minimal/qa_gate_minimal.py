#!/usr/bin/env python3
"""Unit 04-10：五维自动 QA 门禁硬阈值校验极简示范。"""
from __future__ import annotations

import json
import sys


def check_5d_gates(metrics: dict) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if metrics.get("voice_max_dist", 1.0) > 0.15:
        failures.append("声纹距离超过 0.15")
    if metrics.get("voice_f0_spread_hz", 99.0) > 8.0:
        failures.append("基频 F0 极差超过 8.0 Hz")
    if not metrics.get("asr_spoken_ok", False):
        failures.append("Whisper 回读未命中命令行口播规范")
    if metrics.get("cover_dh_mae", 99.0) > 5.0:
        failures.append("Cover-S01 数字人连续性 MAE > 5.0")
    if metrics.get("dh_bg_luma_min", 0.0) < 215.0:
        failures.append("数字人圆环棚拍白底发生串色 (<215)")
    if not metrics.get("portal_all_ok", False):
        failures.append("Playwright 门户验收存在坏链或错图")
    return (len(failures) == 0), failures


if __name__ == "__main__":
    sample = {
        "voice_max_dist": 0.0393,
        "voice_f0_spread_hz": 4.29,
        "asr_spoken_ok": True,
        "cover_dh_mae": 0.29,
        "dh_bg_luma_min": 249.8,
        "portal_all_ok": True,
    }
    ok, errs = check_5d_gates(sample)
    print(json.dumps({"passed": ok, "failures": errs}, ensure_ascii=False, indent=2))
    sys.exit(0 if ok else 1)
