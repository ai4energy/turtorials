# WSL2 下配置 Docker GPU 的两大杀手坑小结（智能体实操沉淀）

## 杀手坑一：严禁在 WSL2 Ubuntu 内安装 `nvidia-driver-*`

- **错误做法**：在 WSL2 Ubuntu 中运行 `sudo apt install nvidia-driver-550` 或 `cuda-drivers`。
- **后果**：直接覆盖并破坏 Windows 宿主机向 `/usr/lib/wsl/lib` 注入的 `libcuda.so` 透传桥接，`nvidia-smi` 与容器 `--gpus all` 立刻失效。
- **正确做法**：显卡驱动只装在 **Windows 宿主机**，WSL2 内只需安装 `nvidia-container-toolkit`（或启用 Docker Desktop WSL2 后端）即可透传。

## 杀手坑二：几十 GB 模型权重绝不留在 `/mnt/c/...`

- **错误做法**：把模型权重放在 `C:\models` 再从 `/mnt/c/models` 挂进 WSL2 容器。
- **后果**：跨 9P 文件系统协议读写大权重文件，加载速度比 WSL2 原生 `ext4` 慢 **5–10 倍**。
- **正确做法**：将只读模型目录放在 WSL2 原生 `ext4` 路径（如 `~/models` 或 `/data/models`），再以 `-v /data/models:/models:ro` 只读挂载。

## GPU 容器三条铁律

1. `--gpus all` 显式透传显卡；
2. `-v /data/models:/models:ro` 只读挂卷大权重，绝不 `COPY` 进镜像；
3. 显存是有限桌面面积，提供 `/unload` 或 `/free` 随时腾桌防 OOM。
