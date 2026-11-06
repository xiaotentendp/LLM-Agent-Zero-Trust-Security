# LLM-Agent-Zero-Trust-Security

## 💡 项目背景
随着大模型（LLM）从单纯的对话走向具有物理执行权限的 Agent（智能体），安全风险急剧上升。提示词注入（Prompt Injection）、越权执行以及上下文污染，是企业在真实物理/工业场景落地 AI 时的致命痛点。

本项目是一个**基于零信任架构的 Agent 安全隔离与状态回滚系统 PoC（概念验证）**，旨在为大模型套上“物理缰绳”。

## 🛡️ 核心架构设计
*   **双通道隔离**：将外部不可信输入（如网页、邮件）与内部可信指令（如用户APP）进行物理隔离，自动施加标签。
*   **动作对象对校验**：不信任模型的智商，只信任系统的规则。底层网关校验模型输出的动作是否越权。
*   **状态快照回滚（Checkpoint）**：一旦检测到恶意注入或危险动作，强制丢弃输出，回滚至上一安全状态。
*   **单向数据流**：核心模型与外部执行环境仅通过单向 JSON 文件交互，防止越权。

## 🎬 实机红蓝对抗演示（最小可行性验证）
【点击观看 B 站实机攻防演示：大语言模型智能体的双通道隔离与状态恢复方法及系统最小可行性验证】 https://www.bilibili.com/video/BV1Q7xR6zEMN

## 🚀 运行说明
1. 确保本地已安装 `Ollama` 并拉取了 `qwen:7b` 模型。
2. 分别启动网关、执行器和靶机脚本：
   ```bash
   python harness_env/security_gateway.py
   python target_env/executor.py
   python target_env/send_task.py

## 📂 快速导航
- [安全网关代码 (harness_env)]([red_blue_demo/harness_env/security_gateway.py](https://github.com/xiaotentendp/LLM-Agent-Zero-Trust-Security/blob/main/red_blue_demo/harness_env/security_gateway.py)
- [外部执行器代码 (target_env)]([red_blue_demo/target_env/executor.py](https://github.com/xiaotentendp/LLM-Agent-Zero-Trust-Security/blob/main/red_blue_demo/target_env/executor.py)
- [模拟输入通道代码 (target_env)]([red_blue_demo/target_env/send_task.py](https://github.com/xiaotentendp/LLM-Agent-Zero-Trust-Security/blob/main/red_blue_demo/target_env/send_task.py)
