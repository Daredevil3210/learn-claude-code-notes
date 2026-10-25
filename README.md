# Learn Claude Code：s01–s06 学习记录

本项目整理了 [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) 的前六章、手写练习和学习摘要，目前学习覆盖 Agent 循环、工具调用、权限检查、Hooks、TodoWrite 任务规划和 Subagent 子任务委派。

这是课程学习整理仓库，并非 Claude Code 官方项目。仓库继续使用原名称 `s01-agent-loop-learning`，后续学习内容在同一仓库内更新。完整课程和第七章起的内容请访问上游仓库。

## 当前学习范围

1. [s01：Agent Loop](s01_agent_loop/README.zh.md) — 模型请求工具、程序执行命令、结果写回消息历史，形成持续运行的循环。
2. [s02：Tool Use](s02_tool_use/README.zh.md) — 工具参数定义、`TOOL_HANDLERS` 分发、文件读写编辑和路径检查。
3. [s03：Permission](s03_permission/README.zh.md) — 拒绝列表、规则匹配和用户审批三道闸门，在执行工具前判断权限。
4. [s04：Hooks](s04_hooks/README.zh.md) — 登记回调，在用户输入、工具执行前后和停止前触发扩展逻辑。
5. [s05：TodoWrite](s05_todo_write/README.zh.md) — 用带状态的任务列表管理计划，在连续三轮未更新计划时向模型追加提醒。
6. [s06：Subagent](s06_subagent/README.zh.md) — 主 Agent 通过 `task` 委派子任务；子 Agent 使用独立消息列表运行，最终文本作为工具结果返回。

每章均提供独立的 `code.py`、中英日教程及 SVG 配图。按章节顺序阅读；运行某一章时，不需要先启动其他章节。

## 文件说明

- `s01_agent_loop/code.py`：可交互运行的教学程序，包含模型调用、命令执行工具和消息历史管理。
- `s01_agent_loop/core.py`：手写核心循环练习片段，依赖调用方提供 `client`、`MODEL`、`SYSTEM`、`TOOLS` 和 `run_bash`，不能独立作为完整 Agent 使用。
- `s01_agent_loop/README.zh.md`：中文教程；同目录提供英文、日文教程及 SVG 配图。
- `s02_tool_use/code.py`：包含命令、读取、写入、编辑和查找五种工具的示例。
- `s02_tool_use/SUMMARY.md`：第二章学习时生成的摘要。
- `s03_permission/code.py`：在工具执行前加入权限判断和审批。
- `s04_hooks/code.py`：Hook 注册表、权限和日志钩子、输出提醒及停止前统计。
- `s05_todo_write/code.py`：任务列表解析、更新校验、状态渲染、`todo_write` 工具和 reminder 计数器。
- `s05_todo_write/example/hello.py`：补充类型注解、文档和主入口的问候程序。
- `s05_todo_write/example/demo_pkg/`：练习生成的文本工具包及单元测试。
- `s06_subagent/code.py`：`task` 工具定义与处理函数、独立消息列表、最多 30 轮的子 Agent 循环及父子共用的工具 Hooks。
- `requirements.txt`：运行 s01–s06 所需的直接依赖，这六章共用一套环境。
- `requirements-dev.txt`：可选测试依赖，运行示例测试时安装。
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

学习后续章节时，选择其中一条运行即可：

```powershell
.\.venv\Scripts\python.exe .\s02_tool_use\code.py
.\.venv\Scripts\python.exe .\s03_permission\code.py
.\.venv\Scripts\python.exe .\s04_hooks\code.py
.\.venv\Scripts\python.exe .\s05_todo_write\code.py
.\.venv\Scripts\python.exe .\s06_subagent\code.py
```

macOS / Linux：

```sh
.venv/bin/python s01_agent_loop/code.py
```

macOS / Linux 可将命令中的章节路径替换为对应的 `s02_tool_use/code.py`、`s03_permission/code.py`、`s04_hooks/code.py`、`s05_todo_write/code.py` 或 `s06_subagent/code.py`。

看到对应的 `s01 >>` 至 `s06 >>` 提示符后输入任务。可以先要求“调用命令工具，只输出 hello-agent，并告诉我实际输出”。输入 `q` 或 `exit` 退出。

第五章可使用任务：`Review Python files under s05_todo_write/example and fix any style issues`。请从仓库根目录启动 Agent，保持任务中的相对路径与当前工作目录一致。

第六章可输入：`Use a subtask to find what testing framework this project uses`。观察 `[Subagent started]`、`[sub]` 和 `[Subagent done]` 输出，再查看主 Agent 返回的结论。这是需要模型 API 的交互练习。

Windows 上工具虽然名为 `bash`，程序实际通过 `cmd.exe` 执行命令，语法与 PowerShell 不同。

## 运行第五章示例测试

测试只覆盖示例包的本地文本函数，不调用模型 API。先在仓库根目录安装可选依赖：

```powershell
uv pip install --python .\.venv\Scripts\python.exe -r requirements-dev.txt
Push-Location .\s05_todo_write\example
..\..\.venv\Scripts\python.exe -m pytest demo_pkg/tests -q
Pop-Location
```

macOS / Linux：

```sh
.venv/bin/python -m pip install -r requirements-dev.txt
(cd s05_todo_write/example && ../../.venv/bin/python -m pytest demo_pkg/tests -q)
```

测试覆盖空白规范化、词数统计、序列分块和文本摘要，以及空输入、边界值和无效参数。

## 学习重点

1. s01：区分外层交互循环和内层 Agent 循环；`TOOLS` 描述能力，工具处理函数执行操作，`tool_use_id` 关联工具请求和结果。
2. s02：理解工具定义与处理函数的分工，以及 `safe_path()` 对文件工具路径的检查。
3. s03：区分“直接拒绝”“需要询问”和“用户决定”，并观察审批发生在工具执行之前。
4. s04：函数保存在 `HOOKS` 的事件列表中；`register_hook()` 登记函数，`trigger_hooks()` 调用函数，事件触发位置的代码处理返回结果。
5. s05：模型通过 `todo_write` 更新完整任务列表；`TodoManager` 先校验再替换旧状态，`render()` 返回可读文字，`run_todo_write()` 打印并返回工具结果。
6. s06：`TASK_TOOL` 向模型说明工具，`TOOLS` 包含它，`TOOL_HANDLERS["task"]` 对应 `run_subagent`；模型提出调用请求后，程序执行函数并返回工具结果。

s04 中的 `context_inject_hook()` 当前只是打印工作目录，没有修改发给模型的消息；`summary_hook()` 统计历史中的 `tool_result` 条目，包含以工具结果形式记录的拒绝信息。`Stop` 钩子返回 `None` 时允许结束，返回非空提示字符串时可请求继续运行。

s05 的计划保存在内存中，每次更新最多 20 项，且最多一项为 `in_progress`；不合法的更新保留旧列表。连续三个工具调用轮次未使用 `todo_write` 时，提醒随工具结果交给模型，然后计数归零。清单记录计划和进度，实际文件操作仍由原有工具执行。

s06 每次调用 `run_subagent(prompt)` 都新建 `messages`，不会自动复制父对话；任务所需信息应写入 `prompt`。主 Agent 同步等待，子 Agent 最终文字作为 `task` 的 `tool_result` 返回，读取文件等中间结果留在子消息列表。父子共用同一模型客户端、工作目录和工具权限 Hooks，文件修改双方可见；子 Agent 没有 `task` 工具，只允许一层委派。最多 30 轮指模型请求次数，一轮可包含多个工具调用；达到上限返回停止提示。

## 运行边界

这些教学示例会真实执行模型生成的系统命令。字符串黑名单和正则匹配不构成完整沙箱；`cwd` 也不限制文件访问范围。s02 的路径检查主要保护文件工具，s03 和 s04 演示权限审批及钩子机制。请在不含重要文件和额外凭据的练习环境中运行。

仓库仅保留 `.env.example` 配置模板；`.env`、环境目录、编辑器配置、缓存和临时练习文件不随版本发布。第五章的正式示例程序和配套测试作为学习成果保留。

## 版本记录

- [v0.4.0](https://github.com/Daredevil3210/s01-agent-loop-learning/releases/tag/v0.4.0)：学习范围扩展到 s06，加入 Subagent 代码、三语教程和配图，补充任务委派、消息隔离及运行说明。
- [v0.3.0](https://github.com/Daredevil3210/s01-agent-loop-learning/releases/tag/v0.3.0)：学习范围扩展到 s05，加入 TodoWrite、第五章示例包及测试，补充可选测试环境和运行步骤。
- [v0.2.0](https://github.com/Daredevil3210/s01-agent-loop-learning/releases/tag/v0.2.0)：学习范围扩展到 s01–s04，加入第二章学习摘要，更新运行说明和章节导航。
- [v0.1.0](https://github.com/Daredevil3210/s01-agent-loop-learning/releases/tag/v0.1.0)：第一章及手写循环练习的首次整理版。

详细变更见 [RELEASE_NOTES.md](RELEASE_NOTES.md)。

## 来源和许可证

课程源码、教程与配图来源于 [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)，整理时上游基准提交为 `ce8f9f186058939da54c9d6fead78dfb5d0fd6c3`。

本整理版保留本地学习代码和第一章程序的本地改动，并收录第二至第六章、第二章学习摘要以及第五章练习成果；已收录章节之间使用本地导航，第六章指向第七章的链接转到上游对应版本。另有独立安装说明与不含密钥的配置模板。未包含原仓库的 Git 历史、第七章起的内容或本地环境。

原作者版权：Copyright (c) 2024 shareAI Lab。代码沿用 [MIT License](LICENSE)；分发时请保留原版权和许可声明。
