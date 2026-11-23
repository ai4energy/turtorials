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
