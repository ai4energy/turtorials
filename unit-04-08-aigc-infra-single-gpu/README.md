# Unit 04-08：原子基座合龙（单卡 WSL2 `docker-compose.yml` 实操）

> 对应第四单元 L1 原子服务第 08 集。16 GB 单卡（如 `gpu4080`）通过环境变量与 `/models:ro` 只读挂卷管理单卡服务；多卡产线只需按模板扩展 YAML 锚点，严禁直接在产线启停改配置。

```bash
cp .env.example .env
chmod 600 .env
docker compose config
# 按需单卡分时拉起（避免 16 GB 显存同时装满多模型）
docker compose --profile voice up -d
```
