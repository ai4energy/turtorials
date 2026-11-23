# 项目协作规范 · Claude Code 记忆模板 (`CLAUDE.md`)

> 将本文件放在项目根目录，Claude Code 启动时会自动读取，不用每次重复交代规矩。

## 1. 核心工作流铁律（先干活 -> 再验收 -> 写 .md 小结）
1. **先动手完成目标并跑通实测**：修改代码或配好环境后，必须亲自执行验证命令（例如 `python -m pytest`、`python -m py_compile`、`curl /api/health`），以真实终端输出作为成功依据。
2. **严禁直接输出真实密钥/公网 IP**：所有配置文件、文档或示例一律使用 `<YOUR_API_KEY>`、`<SERVER_IP>` 占位符。
3. **每次收工必须写入结构化 `.md` 小结**：按「目标与前置 -> 实际执行步骤 -> 验证命令与结果 -> 避坑记录 -> 下次复现一键命令」沉淀到 `docs/` 或 `NOTES.md`。

## 2. 本仓库常用命令与环境约定
- Python 环境：一律使用项目局部 `.venv`（`source .venv/bin/activate`），禁止 `sudo pip`。
- 包安装镜像：`-i https://pypi.tuna.tsinghua.edu.cn/simple`
- Git 提交风格：说明为什么改动；提交前先运行 `git status` 检查不要误提交大体积 `.mp4` / `.zip` / 私钥与 `.env`。
