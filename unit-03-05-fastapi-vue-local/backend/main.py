"""Unit 3 示例后端：轻量 FastAPI 任务清单服务（提供健康检查与增删查接口）。"""
from __future__ import annotations

from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Ai4Energy 全栈任务看板 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=80)
    category: str = Field(default="WSL/Docker")


TASKS: list[dict] = [
    {
        "id": 1,
        "title": "设置 WSL root 密码并验证 apt 部署 Nginx",
        "category": "Linux服务",
        "done": True,
        "created_at": "2026-11-23T00:00:00Z",
    },
    {
        "id": 2,
        "title": "用 Docker Compose 拉起 FastAPI + Vue 双容器",
        "category": "容器编排",
        "done": False,
        "created_at": "2026-11-23T00:05:00Z",
    },
]
_NEXT_ID = 3


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "fastapi-backend", "count": len(TASKS)}


@app.get("/api/tasks")
def list_tasks():
    return {"items": TASKS}


@app.post("/api/tasks", status_code=201)
def create_task(payload: TaskCreate):
    global _NEXT_ID
    item = {
        "id": _NEXT_ID,
        "title": payload.title.strip(),
        "category": payload.category.strip() or "通用",
        "done": False,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    _NEXT_ID += 1
    TASKS.append(item)
    return item


@app.post("/api/tasks/{task_id}/toggle")
def toggle_task(task_id: int):
    for t in TASKS:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    global TASKS
    before = len(TASKS)
    TASKS = [t for t in TASKS if t["id"] != task_id]
    if len(TASKS) == before:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"deleted": task_id}
