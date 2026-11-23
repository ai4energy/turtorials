# 第三单元 第 5 集：本地前后端分离开发（Python FastAPI + Vue 3）

## 1. 启动 Python FastAPI 后端

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
uvicorn main:app --reload --port 8000
# 接口文档: http://127.0.0.1:8000/docs
```

## 2. 启动 Vue 3 前端网页

- **方式 A（零 Node 快速体验，使用原生 `vue.global.prod.js`）**：
  ```bash
  cd frontend && python3 -m http.server 5173
  # 浏览器打开 http://127.0.0.1:5173 （自动请求 http://127.0.0.1:8000/api/tasks）
  ```
- **方式 B（标准 Vite + `.vue` 单文件组件工程）**：见 [`frontend-vite/`](frontend-vite/src/App.vue)。
