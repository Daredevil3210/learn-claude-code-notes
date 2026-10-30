# Learn Claude Code Notes

[English](README.md) | **简体中文**

基于 [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) 的编程 Agent 学习仓库，整理章节实现、教程、配图、练习与实现笔记，帮助理解 Agent 如何调用工具并完成任务。

**当前范围：** s01–s09 · **建议 Python 版本：** 3.13 · **许可证：** MIT

本仓库是基于上游课程的独立学习整理项目，不属于 Anthropic 或 Claude Code 官方产品。各章是可独立运行的教学示例，并非一个集成所有能力的应用。

## 章节导航

1. [s01 · Agent Loop](s01_agent_loop/README.zh.md) — 模型请求、工具执行与对话历史组成的核心循环。
2. [s02 · Tool Use](s02_tool_use/README.zh.md) — 工具参数定义、处理函数分发与文件操作。
3. [s03 · Permission](s03_permission/README.zh.md) — 拒绝列表、权限规则与用户审批。
4. [s04 · Hooks](s04_hooks/README.zh.md) — 用户输入、工具执行和停止前后的回调机制。
5. [s05 · TodoWrite](s05_todo_write/README.zh.md) — 任务规划、状态校验与更新提醒。
6. [s06 · Subagent](s06_subagent/README.zh.md) — 使用独立对话历史执行委派的子任务。
7. [s07 · Skill Loading](s07_skill_loading/README.zh.md) — 技能目录与按需加载完整说明。
8. [s08 · Context Compact](s08_context_compact/README.zh.md) — 工具输出预算、历史摘要与上下文过长后的恢复。
9. [s09 · Memory](s09_memory/README.zh.md) — 跨会话知识存储、相关记忆召回、提取与整理。

每章包含可运行的 `code.py`、中英日教程和 SVG 配图。s10 及后续内容请参阅[上游课程](https://github.com/shareAI-lab/learn-claude-code)。建议先阅读教程，再对照源码，最后用小任务观察工具调用及结果如何进入循环。

## 快速开始

需要 Git、Python 3.13，以及支持工具调用的模型和对应 API 凭据。程序通过 Anthropic API 或兼容接口调用模型，运行依赖为 `anthropic`、`python-dotenv` 和 `PyYAML`。

### 1. 克隆仓库

```sh
git clone https://github.com/Daredevil3210/learn-claude-code-notes.git
cd learn-claude-code-notes
```

### 2. 创建环境并安装依赖

Windows PowerShell：

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

如果已经使用 `uv`，可将前两条命令替换为 `uv venv --python 3.13 .venv` 和 `uv pip install --python .venv -r requirements.txt`。配置模板仅在首次安装时复制；更新项目时保留已有 `.env`。

### 3. 配置模型

参考 [.env.example](.env.example)，编辑本地 `.env`：

- `ANTHROPIC_API_KEY`：你的 API 密钥。
- `MODEL_ID`：服务商账户可用且支持工具调用的模型名称。
- `ANTHROPIC_BASE_URL`：可选的 Anthropic 兼容 API 地址。

仅提供 OpenAI 兼容接口的服务不能直接用于这些脚本。模型请求可能计费；上下文摘要、记忆选择、提取和整理也可能产生额外请求。

### 4. 运行章节

请从**仓库根目录**启动，使相对路径、技能目录和记忆文件的位置保持一致。

Windows PowerShell：

```powershell
.\.venv\Scripts\python.exe .\s01_agent_loop\code.py
```

macOS / Linux：

```sh
.venv/bin/python s01_agent_loop/code.py
```

将章节路径替换为例如 `s09_memory/code.py`，即可运行对应章节。在提示符后输入任务，输入 `q` 或 `exit` 退出；无需先启动前面的章节。Windows 中名为 `bash` 的工具实际通过 `cmd.exe` 执行命令，应使用 cmd 语法。

## 练习建议

- **s05：** 输入 `Review Python files under s05_todo_write/example and fix any style issues`，观察文件操作与任务状态更新。
- **s06：** 输入 `Use a subtask to find what testing framework this project uses`，跟踪子 Agent 执行过程和最终回复。
- **s07：** 先问 `What skills are available?`，再输入 `Load the code-review skill and follow its instructions`。从仓库根目录启动，以便找到 `skills/`。
- **s08：** 要求比较 s01～s05 各章 README 的一级标题，然后调用 `compact` 工具。自动压缩需要达到阈值，短任务不一定触发。上游练习文件 `web/src/data/generated/docs.json` 未收录于本仓库。
- **s09：** 输入 `I prefer using tabs for indentation. Remember that.`，检查 `.memory/`，退出并重新启动，再问 `What indentation style do I prefer?`。提取结果取决于模型输出，应检查实际文件；`Do not create files in this session.` 这样的临时要求不应成为长期偏好。

## 仓库内容

- `s01_agent_loop/` 至 `s09_memory/`：章节代码、教程与配图。
- [s01 核心循环练习](s01_agent_loop/core.py)：手写片段，需要调用方提供依赖，不能独立运行。
- [s02 学习摘要](s02_tool_use/SUMMARY.md)：第二章中文学习记录。
- [s05 示例](s05_todo_write/example/)：问候程序、文本工具包及其单元测试。
- [s06 字符串工具](s06_subagent/example/string_tools.py)：包含文档示例的 `slugify()` 练习。
- [skills](skills/)：Agent 构建、代码审查、PDF 和 MCP 开发的示例技能。Agent 构建参考代码是独立教学资源，部分使用 `MODEL_NAME`；主章节使用 `MODEL_ID`。
- [详细学习笔记](docs/learning-notes.zh.md)：各章节的实现细节和能力边界。
- [运行依赖](requirements.txt)、[测试依赖](requirements-dev.txt)与[配置模板](.env.example)。

技能文档可能提及额外工具和库，仅在执行相应任务时按需安装。

## 本地测试

以下练习测试不调用模型 API。

Windows PowerShell，从仓库根目录执行：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
Push-Location .\s05_todo_write\example
..\..\.venv\Scripts\python.exe -m pytest demo_pkg/tests -q
Pop-Location
.\.venv\Scripts\python.exe -m doctest -v .\s06_subagent\example\string_tools.py
```

macOS / Linux：

```sh
.venv/bin/python -m pip install -r requirements-dev.txt
(cd s05_todo_write/example && ../../.venv/bin/python -m pytest demo_pkg/tests -q)
.venv/bin/python -m doctest -v s06_subagent/example/string_tools.py
```

示例包含 26 项 pytest 测试和 3 个 doctest 用例。各版本的验证范围见 [RELEASE_NOTES.md](RELEASE_NOTES.md)。

## 执行与数据管理

教学程序能够执行命令并修改本地文件。权限检查用于演示 Agent 设计，不构成完整的系统沙箱。请使用不含重要文件或额外凭据的练习环境。

真实 `.env`、凭据、虚拟环境、缓存和运行数据不纳入版本控制。运行数据包括 `.memory/` 中的长期知识、`.transcripts/` 中的对话归档，以及 `.task_outputs/` 中的工具输出；仓库仅提供含占位符的 `.env.example`。

Memory 保存跨会话知识，上下文压缩管理当前对话长度。独立的 s09 程序没有集成 s08 的压缩流程；记忆整理使用内存快照尝试恢复，不是可应对程序崩溃的持久备份。

## 版本记录

完整历史见 [GitHub Releases](https://github.com/Daredevil3210/learn-claude-code-notes/releases) 和[发布说明](RELEASE_NOTES.md)。[v0.7.0](https://github.com/Daredevil3210/learn-claude-code-notes/releases/tag/v0.7.0) 新增 s09 Memory。

仓库原名为 `s01-agent-loop-learning`，现随学习范围扩展而更名。既有提交、标签和发布版本均保留。

## 来源与许可证

课程实现、教程和配图来源于 [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)，以其提交 [`ce8f9f1`](https://github.com/shareAI-lab/learn-claude-code/commit/ce8f9f186058939da54c9d6fead78dfb5d0fd6c3) 为整理基准。本仓库补充学习笔记、本地练习和环境说明，并保留第一章的本地代码修改。

采用 [MIT License](LICENSE)。原作者版权：Copyright (c) 2024 shareAI Lab。再次分发时请保留原版权和许可声明。
