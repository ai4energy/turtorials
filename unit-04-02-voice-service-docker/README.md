# Unit 04-02：WSL2 配通 Docker GPU 与语音服务容器化

> 对应第四单元 L1 原子服务第 02 集。重点：**让智能体配通 `docker run --gpus all ... nvidia-smi` → 验收 → 写本避坑小结 → 容器化封装 HTTP 语音服务**。

## 快速运行

```bash
# 1. 先验 GPU 透传（必须通过）
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi

# 2. 构建并启动单卡语音服务（只读挂卷模型，绝不 COPY 进镜像）
docker build -t single-voice:demo .
docker run -d --name single-voice --gpus all \
  -p 18110:8110 \
  -e HF_HUB_OFFLINE=1 \
  -v /data/models:/models:ro \
  single-voice:demo

# 3. 测通健康与卸载显存接口
curl --noproxy "*" http://127.0.0.1:18110/health
curl --noproxy "*" -X POST http://127.0.0.1:18110/unload
```
