#!/usr/bin/env python3
"""Unit 04-02：单卡 HTTP 语音原子服务精简示范（/health, /tts, /clone, /asr, /unload）。"""
from __future__ import annotations

import gc
import os
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Single-GPU Voice Atomic Service")
_STATE: dict[str, object] = {"loaded": False, "model_dir": os.environ.get("VOICE_MODEL_DIR", "/models/voice/voxcpm2")}


class TTSReq(BaseModel):
    text: str
    ref_wav: str = "ref_01.wav"


@app.get("/health")
def health() -> dict:
    return {
        "ok": True,
        "loaded": _STATE["loaded"],
        "model_exists": Path(str(_STATE["model_dir"])).exists(),
        "offline": os.environ.get("HF_HUB_OFFLINE", "1") == "1",
    }


@app.post("/tts")
def tts(req: TTSReq) -> dict:
    _STATE["loaded"] = True
    return {"ok": True, "text": req.text, "ref": req.ref_wav, "sample_rate": 48000}


@app.post("/unload")
def unload() -> dict:
    _STATE["loaded"] = False
    gc.collect()
    return {"ok": True, "vram_released": True}
