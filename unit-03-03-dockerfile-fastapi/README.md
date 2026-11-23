# 第三单元 第 3 集：编写 Dockerfile 制作自己的 Python FastAPI 镜像

```bash
docker build -t ai4e-fastapi-demo:1.0 .
docker run -d --name api_demo -p 8000:8000 ai4e-fastapi-demo:1.0
curl http://127.0.0.1:8000/api/health
```
