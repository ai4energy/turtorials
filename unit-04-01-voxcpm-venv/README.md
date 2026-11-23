# Unit 04-01：借助 Claude Code 搭 `.venv` 并在单卡本地拉起 VoxCPM2（10 秒样片第 1 步）

> 对应第四单元 L1 原子服务第 01 集。全程国内免代理：`HF_HUB_OFFLINE=1` + 清华 PyPI 源。

## 一、 核心步骤

```bash
python3 -m venv .venv-voice
source .venv-voice/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple voxcpm soundfile numpy

export HF_HUB_OFFLINE=1
python clone_10s_sample.py \
  --model /data/models/voice/voxcpm2 \
  --ref ref_01.wav \
  --text "十秒样片第一拍：单卡也能稳定跑通语音克隆。" \
  --out sample_01.wav
```

## 二、 交付验证

1. 确认生成 `sample_01.wav` 时长约 `3–5s`、`48kHz / 44.1kHz` 可播放；
2. 验收通过后让智能体撰写 `voxcpm2-venv-summary.md` 沉淀环境变量与避坑点。
