# S01 Agent Loop：最小编程 Agent 学习项目

本项目整理了 [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) 的第一章及本地学习练习，用于理解模型调用、工具执行和消息反馈如何组成一个 Agent 循环。

这是原课程第一章的学习整理版，并非 Claude Code 官方项目。完整课程和后续章节请访问上游仓库。

## 文件说明

- `s01_agent_loop/code.py`：可交互运行的教学程序，包含模型调用、命令执行工具和消息历史管理。
- `s01_agent_loop/core.py`：手写核心循环练习片段，依赖调用方提供 `client`、`MODEL`、`SYSTEM`、`TOOLS` 和 `run_bash`，不能独立作为完整 Agent 使用。
- `s01_agent_loop/README.zh.md`：中文教程；同目录提供英文、日文教程及 SVG 配图。
- `requirements.txt`：运行第一章所需的直接依赖。
- `.python-version`：建议使用的 Python 版本。
- `.env.example`：配置模板，不包含真实密钥。
- `LICENSE`：原项目的 MIT 许可证及版权声明。

## 环境准备

建议使用 Python 3.13。需要可访问的模型 API、对应密钥以及支持工具调用的模型。本项目通过 Anthropic SDK 调用接口；使用其他服务商时，需要其 Anthropic 兼容接口。

在仓库根目录打开 PowerShell，使用已经安装好的 uv：

```powershell
uv venv --python 3.13 .venv
uv pip install --python .\.venv\Scripts\python.exe -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

没有 uv 时，也可使用已有的 Python 3.13：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

macOS / Linux：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
```

编辑 `.env`，将 `ANTHROPIC_API_KEY` 替换为自己的密钥，将 `MODEL_ID` 设置为账户可用的模型名称。使用兼容服务商时，再取消 `ANTHROPIC_BASE_URL` 行的注释，并填写该服务商的 Anthropic 兼容接口地址。

API 请求可能计费。不要将 `.env`、真实密钥或个人数据提交到仓库。

## 运行

在仓库根目录执行：

```powershell
.\.venv\Scripts\python.exe .\s01_agent_loop\code.py
```

macOS / Linux：

```sh
.venv/bin/python s01_agent_loop/code.py
```

看到 `s01 >>` 后输入任务。可以先要求“调用命令工具，只输出 hello-agent，并告诉我实际输出”。输入 `q` 或 `exit` 退出。

Windows 上工具虽然名为 `bash`，程序实际通过 `cmd.exe` 执行命令，语法与 PowerShell 不同。

## 学习重点

1. 外层循环接收用户输入，内层循环完成同一个任务中的多次模型和工具交互。
2. `TOOLS` 描述工具能力，`run_bash()` 才实际执行命令。
3. `tool_use_id` 将工具结果与对应请求关联。
4. 工具结果写入消息历史后，会随下一次模型调用发送。

## 运行边界

这是教学示例，会真实执行模型生成的系统命令。字符串黑名单不构成可靠沙箱；`cwd` 也不限制文件访问范围。请在不含重要文件和额外凭据的练习环境中运行。第一章不包含完整的权限审批和生产部署机制。

## 来源和许可证

课程源码、教程与配图来源于 [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)，整理时上游基准提交为 `ce8f9f186058939da54c9d6fead78dfb5d0fd6c3`。

本整理版保留本地学习代码和第一章程序的本地改动；教程中指向第二章的相对链接改为上游链接，并新增独立安装说明与配置模板。未包含原仓库的 Git 历史、其他章节或本地环境。

原作者版权：Copyright (c) 2024 shareAI Lab。代码沿用 [MIT License](LICENSE)；分发时请保留原版权和许可声明。
