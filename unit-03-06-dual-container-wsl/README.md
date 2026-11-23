# 第三单元双容器实战示例：FastAPI 后端 + Vue/Nginx 前端

## 1. 本地前后端分离调试（第 5 集）

```bash
# 终端 1：启动后端 FastAPI
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
uvicorn main:app --reload --port 8000

# 终端 2：启动静态前端页面（或直接打开 frontend/index.html）
cd frontend && python3 -m http.server 5173
```

## 2. 一键打包为双容器并在 WSL 运行（第 6 集）

```bash
docker compose up -d --build
# 浏览器打开 http://localhost:8088 （接口文档：http://localhost:8088/docs）
docker compose ps
docker compose down
```
