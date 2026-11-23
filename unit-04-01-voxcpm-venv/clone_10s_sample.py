#!/usr/bin/env python3
"""Unit 04-01：10 秒微型样片单卡本地 VoxCPM2 音色克隆最小脚本（HF_HUB_OFFLINE=1）。"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="/data/models/voice/voxcpm2")
    ap.add_argument("--ref", required=True, help="参考音 .wav 路径")
    ap.add_argument("--text", default="十秒样片第一拍：单卡本地语音克隆已跑通。")
    ap.add_argument("--out", default="sample_01.wav")
    ap.add_argument("--device", default="cuda:0")
    args = ap.parse_args()

    import numpy as np
    import soundfile as sf
    from voxcpm import VoxCPM

    model = VoxCPM(
        voxcpm_model_path=args.model,
        zipenhancer_model_path=None,
        enable_denoiser=False,
        device=args.device,
        optimize=args.device.startswith("cuda"),
    )
    wav = model.generate(
        text=args.text,
        reference_wav_path=str(Path(args.ref).resolve()),
        cfg_value=2.0,
        inference_timesteps=15,
    )
    sr = int(model.tts_model.sample_rate)
    sf.write(args.out, np.asarray(wav, dtype=np.float32), sr)
    print(f"OK: wrote {args.out} ({len(wav)/sr:.2f}s @ {sr}Hz)")


if __name__ == "__main__":
    main()
