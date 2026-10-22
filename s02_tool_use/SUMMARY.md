# s02: Tool Use — 章节摘要

> 生成依据：`README.md` + `code.py`。
> 环境说明：本章目录不单独维护依赖文件，运行时统一使用仓库根目录的 [`requirements.txt`](../requirements.txt)。本摘要的依赖说明由 `code.py` 的 import 整理。

## 一句话概括

s01 只有一个 `bash` 工具的智能体，在 s02 扩展为 5 个专用工具，而**主循环一行未改**——唯一的变化是把硬编码的 `run_bash(block.input["command"])` 换成 `TOOL_HANDLERS[block.name](**block.input)` 字典分发。

## 核心论点

"加一个工具，只加一个 handler。" 加工具 = 两步：

1. 在 `TOOLS` 数组里加一条 JSON schema（告诉模型"我能做什么"）；
2. 在 `TOOL_HANDLERS` 字典里加一行「工具名 → 处理函数」的映射。

## 5 个工具

| 工具 | 处理函数 | 作用 |
|------|---------|------|
| `bash` | `run_bash` | 执行 shell 命令（cmd.exe，120s 超时，输出截断 50000 字符） |
| `read_file` | `run_read` | 读文件，`limit` 限制行数并提示剩余行数 |
| `write_file` | `run_write` | 写文件，自动创建父目录 |
| `edit_file` | `run_edit` | 精确文本替换一次，找不到则返回错误 |
| `glob` | `run_glob` | 按模式递归查找文件（`**` 递归，最多显示 200 条） |

## 与 s01 的差异

| 组件 | s01 | s02 |
|------|-----|-----|
| 工具数量 | 1（bash） | 5（+read / write / edit / glob） |
| 工具执行 | 硬编码 `run_bash()` | `TOOL_HANDLERS` 分发查找 |
| 路径安全 | 无 | `safe_path` 校验（仅文件工具） |
| 主循环 | `while True` + `tool_use` 检测 | 与 s01 完全一致 |

## 两个实现细节

- **路径安全**：`safe_path()` 用 `resolve()` + `is_relative_to(WORKDIR)` 把文件工具锁在工作目录内，越界直接抛 `Path escapes workspace`。`run_glob` 的结果也做了同样的过滤，防止匹配到符号链接指向的外部路径。
- **多工具调用**：模型可在一次响应中返回多个 `tool_use` 块，代码按它们在 `response.content` 中的原始顺序依次执行，最后汇总成一个 `user` 消息（多个 `tool_result`）回灌给模型。

## 遗留问题（通往 s03）

文件工具有 `safe_path` 保护，但 `bash` 只做了一份危险命令黑名单（`rm -rf /`、`sudo`、`shutdown`、`reboot`、`> /dev/`），**其余仍然畅通**。s03 会加上权限闸门：执行前先判断"这个操作安全吗？需要用户批准吗？"。

## 依赖（由 import 反推）

- 第三方：`anthropic`（`Anthropic` 客户端）、`python-dotenv`（`load_dotenv`）
- 标准库：`os`、`subprocess`、`pathlib`、`glob`、`readline`（可选，缺失时静默跳过）
- 环境变量：`MODEL_ID`（必填）、`ANTHROPIC_BASE_URL`（可选，设置时会清除 `ANTHROPIC_AUTH_TOKEN`）

## 运行

```sh
python s02_tool_use/code.py
```
