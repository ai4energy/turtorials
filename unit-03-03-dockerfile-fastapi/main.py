"""第三单元第 3 集：极简单容器 FastAPI 镜像制作示例。"""
from fastapi import FastAPI

app = FastAPI(title="Ai4Energy Dockerfile Demo API")


@app.get("/api/health")
def health():
    return {"status": "ok", "source": "github.com/ai4energy/turtorials/unit-03-03-dockerfile-fastapi"}
