FROM python:3.11-slim

WORKDIR /app
ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple \
    HF_HUB_OFFLINE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir fastapi uvicorn soundfile numpy
COPY app.py /app/app.py

EXPOSE 8110
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8110"]
