# Unit 04-04：ComfyUI 双重面孔（GUI vs API JSON）与 `lowvram` 容器化

> 对应第四单元 L1 原子服务第 04 集。16 GB 单卡（如 RTX 4080）锁定 `fp8`/`GGUF` 量化模型与 `VRAM_MODE=lowvram`，并通过 `POST /prompt` 与 `POST /free` 实现程序化调度与显存清理。

```bash
python run_comfy_api.py --url http://127.0.0.1:18130 --workflow workflow_api.json --free-after
```
