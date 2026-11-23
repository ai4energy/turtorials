# Unit 04-07：全厂胶水与 AI 之手（`ffmpeg` 五大焊法 + `vncdotool` / Playwright 自动录屏）

> 对应第四单元 L1 原子服务第 07 集。

1. **`ffmpeg` 五大底层焊法**：响度归一 (`-16 LUFS`)、分拍拼接 (`setpts/tpad`)、红圈与 2× 字幕叠层 (`overlay=enable='between(t,...)'`)、`<=18s` 数字人切片 `xfade`、关键帧抽图 (`-vframes 1`)。
2. **双栖自动录屏**：网页端用 Playwright `recordVideo` + DOM 红圈；桌面端用 `vncdotool` 连 VNC 截屏、`mouseMove`/`mousePress`、`keyPress` 零人工录屏。
