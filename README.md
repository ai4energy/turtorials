# Ai4Energy 实战课程代码仓库 (`ai4energy/turtorials`)

> 配套《AI 智能体、Linux 服务、Docker 与前后端双容器实战》全套公开课与离线门户使用；每个子目录严格对应课程章节，所有代码均已实测通过并可直接运行。

```bash
git clone https://github.com/ai4energy/turtorials.git
cd turtorials
```

---

## 子目录与课程分集对应索引

| 子目录 | 对应课程模块 | 核心代码清单 |
| :--- | :--- | :--- |
| [`unit-02-ai-agents-templates/`](unit-02-ai-agents-templates/README.md) | **第二单元 · 01–05 集**<br/>AI 智能体与元能力 | 脱敏模板 `CLAUDE.md`、`AGENTS.md`、`opencode.jsonc`、`summary-prompt.md` |
| [`unit-03-01-wsl-nginx/`](unit-03-01-wsl-nginx/README.md) | **第三单元 · 第 1 集**<br/>WSL `root` + `apt` 装 Nginx | `setup_nginx.sh`、`index.html` |
| [`unit-03-02-docker-basics/`](unit-03-02-docker-basics/README.md) | **第三单元 · 第 2 集**<br/>Docker 镜像与 `-p`/`-v` 挂载 | `run_demo.sh`、`html/index.html` |
| [`unit-03-03-dockerfile-fastapi/`](unit-03-03-dockerfile-fastapi/README.md) | **第三单元 · 第 3 集**<br/>制作自定义 Python 镜像 | `main.py`、`requirements.txt`、`Dockerfile`、`.dockerignore` |
| [`unit-03-04-docker-compose/`](unit-03-04-docker-compose/README.md) | **第三单元 · 第 4 集**<br/>多容器编排 | 声明式 `docker-compose.yml`（服务名互通与健康检查） |
| [`unit-03-05-fastapi-vue-local/`](unit-03-05-fastapi-vue-local/README.md) | **第三单元 · 第 5 集**<br/>本地 FastAPI + Vue 3 联调 | `backend/` (`FastAPI` REST + CORS) + `frontend/` (`Vue 3`) + `frontend-vite/` (`App.vue` SFC 工程) |
| [`unit-03-06-dual-container-wsl/`](unit-03-06-dual-container-wsl/README.md) | **第三单元 · 第 6 集（收官）**<br/>双容器落地 WSL 闭环 | `backend/Dockerfile` + `frontend/Dockerfile` (`Vue 3 + Nginx /api/ 反代`) + `docker-compose.yml` |
| [`unit-04-01-voxcpm-venv/`](unit-04-01-voxcpm-venv/README.md) | **第四单元 · 第 1 集（L1 原子）**<br/>`.venv` 本地拉起 VoxCPM2 | `clone_10s_sample.py`（`HF_HUB_OFFLINE=1` + 清华源单卡克隆 10 秒样片） |
| [`unit-04-02-voice-service-docker/`](unit-04-02-voice-service-docker/README.md) | **第四单元 · 第 2 集（L1 原子）**<br/>WSL2 Docker GPU 与语音容器 | `docker-gpu-wsl2-pitfalls-summary.md`、`Dockerfile`、`app.py`（`/tts` `/unload`） |
| [`unit-04-04-comfyui-api-workflow/`](unit-04-04-comfyui-api-workflow/README.md) | **第四单元 · 第 4 集（L1 原子）**<br/>ComfyUI API JSON + `lowvram` | `run_comfy_api.py`、`workflow_api.json`（`POST /prompt` + `/free`） |
| [`unit-04-05-vlm-visual-loop/`](unit-04-05-vlm-visual-loop/README.md) | **第四单元 · 第 5 集（L1 原子）**<br/>7B 识图与「识图反复」闭环 | `vlm_visual_loop.py`（0–1000 归一化坐标定位 + 截图复检直到 PASS） |
| [`unit-04-06-manim-20line-card/`](unit-04-06-manim-20line-card/README.md) | **第四单元 · 第 6 集（L1 原子）**<br/>20 行 Python Manim 动态片头卡 | `intro_card_20lines.py`（1080p@25fps 浅色中文卡片） |
| [`unit-04-07-ffmpeg-vncdotool-weld/`](unit-04-07-ffmpeg-vncdotool-weld/README.md) | **第四单元 · 第 7 集（L1 原子）**<br/>`ffmpeg` 五大焊法与 `vncdotool` | `weld_and_vnc_demo.py`（`-16 LUFS`、`overlay` 与 VNC 自动点击录屏） |
| [`unit-04-08-aigc-infra-single-gpu/`](unit-04-08-aigc-infra-single-gpu/README.md) | **第四单元 · 第 8 集（L1 合龙）**<br/>单卡 WSL2 `docker-compose.yml` | `docker-compose.yml`、`.env.example`（`--profile` 分时与 `/models:ro` 挂卷） |
| [`unit-04-10-qa-gate-minimal/`](unit-04-10-qa-gate-minimal/README.md) | **第四单元 · 第 10 集（L2 平台）**<br/>五维自动 QA 门禁校验 | `qa_gate_minimal.py`（声纹、F0、ASR、Cover MAE、白底亮度、门户验收） |
| [`unit-04-13-studio-mcp-50line/`](unit-04-13-studio-mcp-50line/README.md) | **第四单元 · 第 13 集（L4 智能体）**<br/>50 行极简 Studio MCP | `minimal_studio_mcp.py`（对比 L3 网页与 L4 AI 工具暴露） |
| [`unit-04-14-tmux-agent-runner/`](unit-04-14-tmux-agent-runner/README.md) | **第四单元 · 第 14 集（L4 智能体）**<br/>免代理 `tmux` 无人值守跑批 | `run_tmux_batch.sh`（持久化会话 + `nvidia-smi` 显存守卫） |
