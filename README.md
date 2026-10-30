# Learn Claude Code Notes

**English** | [简体中文](README.zh.md)

A study repository for understanding how coding agents work, based on [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code). It brings together chapter implementations, tutorials, diagrams, exercises, and implementation notes.

**Current coverage:** s01–s09 · **Suggested Python:** 3.13 · **License:** MIT

This is an independent learning repository derived from the upstream course. It is not an official Anthropic or Claude Code product. Chapters are standalone teaching examples rather than a single integrated application.

## Curriculum

1. [s01 · Agent Loop](s01_agent_loop/README.md) — Model requests, tool execution, and conversation history.
2. [s02 · Tool Use](s02_tool_use/README.md) — Tool schemas, dispatch, and file operations.
3. [s03 · Permission](s03_permission/README.md) — Deny lists, permission rules, and user approval.
4. [s04 · Hooks](s04_hooks/README.md) — Callbacks around user input, tool execution, and stopping.
5. [s05 · TodoWrite](s05_todo_write/README.md) — Task planning, status validation, and reminders.
6. [s06 · Subagent](s06_subagent/README.md) — Delegated tasks with separate conversation histories.
7. [s07 · Skill Loading](s07_skill_loading/README.md) — Skill catalogs and on-demand instruction loading.
8. [s08 · Context Compact](s08_context_compact/README.md) — Tool-output budgets, history summaries, and context recovery.
9. [s09 · Memory](s09_memory/README.md) — Persistent knowledge, selective recall, extraction, and consolidation.

Each chapter contains a runnable `code.py`, English/Chinese/Japanese tutorials, and SVG diagrams. Chapters s10 onward are available in the [upstream course](https://github.com/shareAI-lab/learn-claude-code). Read a chapter's tutorial, inspect its implementation, then try a small task and follow the tool results through the loop.

## Quick start

You need Git, Python 3.13, and credentials for a tool-capable model accessible through the Anthropic API or an Anthropic-compatible endpoint. The runtime dependencies are `anthropic`, `python-dotenv`, and `PyYAML`.

### 1. Clone the repository

```sh
git clone https://github.com/Daredevil3210/learn-claude-code-notes.git
cd learn-claude-code-notes
```

### 2. Create an environment and install dependencies

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

macOS / Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
```

If you already use `uv`, replace the first two commands with `uv venv --python 3.13 .venv` and `uv pip install --python .venv -r requirements.txt`. Copy the configuration template only during initial setup; preserve your existing `.env` when updating.

### 3. Configure the model

Edit the local `.env` using [.env.example](.env.example):

- `ANTHROPIC_API_KEY`: your API key.
- `MODEL_ID`: a model identifier available from your provider, with tool-call support.
- `ANTHROPIC_BASE_URL`: optional Anthropic-compatible API endpoint.

An OpenAI-compatible endpoint alone is not sufficient for these scripts. Model requests may incur charges. Context summarization and memory selection, extraction, and consolidation can make additional model requests.

### 4. Run a chapter

Run from the **repository root** so relative paths, skills, and memory files resolve consistently.

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe .\s01_agent_loop\code.py
```

macOS / Linux:

```sh
.venv/bin/python s01_agent_loop/code.py
```

Replace the chapter path to run another lesson, such as `s09_memory/code.py`. Enter a task at the chapter prompt; type `q` or `exit` to quit. You do not need to start earlier chapters first. On Windows, the tool named `bash` executes through `cmd.exe`, so its commands use cmd syntax.

## Suggested exercises

- **s05:** `Review Python files under s05_todo_write/example and fix any style issues`. Observe task status updates alongside file operations.
- **s06:** `Use a subtask to find what testing framework this project uses`. Follow the subagent's execution and final response.
- **s07:** Ask `What skills are available?`, then `Load the code-review skill and follow its instructions`. Start from the repository root so the `skills/` directory is found.
- **s08:** Ask the agent to compare the top-level headings in the README files for s01–s05, then request the `compact` tool. Automatic compaction requires reaching its thresholds; a short task may not trigger it. The upstream exercise file `web/src/data/generated/docs.json` is not included here.
- **s09:** Say `I prefer using tabs for indentation. Remember that.`, inspect `.memory/`, quit, restart, and ask `What indentation style do I prefer?`. Check actual stored files because extraction depends on model output. Temporary instructions such as `Do not create files in this session.` should not become persistent preferences.

## Repository contents

- `s01_agent_loop/` through `s09_memory/`: chapter code, tutorials, and diagrams.
- [s01 core exercise](s01_agent_loop/core.py): a handwritten loop fragment that requires caller-provided dependencies; it is not a standalone program.
- [s02 summary](s02_tool_use/SUMMARY.md): learning-session notes in Chinese.
- [s05 examples](s05_todo_write/example/): a greeting program and a text utility package with tests.
- [s06 string tools](s06_subagent/example/string_tools.py): a `slugify()` exercise with doctest examples.
- [skills](skills/): sample skills for agent building, code review, PDF tasks, and MCP development. The agent-building references are separate teaching resources; some use `MODEL_NAME`, while chapter programs use `MODEL_ID`.
- [Detailed learning notes (Chinese)](docs/learning-notes.zh.md): implementation details and chapter boundaries.
- [Runtime dependencies](requirements.txt), [test dependencies](requirements-dev.txt), and [configuration template](.env.example).

Skill documents may describe additional tools or libraries; install those only when performing the corresponding tasks.

## Local tests

These exercise tests do not call a model API.

Windows PowerShell, from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
Push-Location .\s05_todo_write\example
..\..\.venv\Scripts\python.exe -m pytest demo_pkg/tests -q
Pop-Location
.\.venv\Scripts\python.exe -m doctest -v .\s06_subagent\example\string_tools.py
```

macOS / Linux:

```sh
.venv/bin/python -m pip install -r requirements-dev.txt
(cd s05_todo_write/example && ../../.venv/bin/python -m pytest demo_pkg/tests -q)
.venv/bin/python -m doctest -v s06_subagent/example/string_tools.py
```

The included examples contain 26 pytest tests and 3 doctest cases. Release-specific validation is documented in [RELEASE_NOTES.md](RELEASE_NOTES.md).

## Execution and data handling

The examples can execute commands and modify local files. Their permission checks demonstrate agent design and do not provide a complete system sandbox. Use a disposable practice workspace without important files or unrelated credentials.

Real `.env` files, credentials, virtual environments, caches, and runtime data are excluded from version control. Runtime data includes `.memory/` for persistent knowledge, `.transcripts/` for archived conversations, and `.task_outputs/` for saved tool results. Only the placeholder `.env.example` is included.

Memory stores selected knowledge across sessions; context compaction manages the current conversation. The standalone s09 program does not integrate the s08 compaction pipeline. Memory consolidation uses an in-memory recovery snapshot, not a crash-safe backup.

## Releases

See [GitHub Releases](https://github.com/Daredevil3210/learn-claude-code-notes/releases) and the [release notes](RELEASE_NOTES.md) for the version history. Version [v0.7.0](https://github.com/Daredevil3210/learn-claude-code-notes/releases/tag/v0.7.0) added s09 Memory.

The repository was originally named `s01-agent-loop-learning` and was renamed as its learning scope expanded. Existing commits, tags, and releases are retained.

## Attribution and license

Course implementations, tutorials, and diagrams originate from [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code), using upstream revision [`ce8f9f1`](https://github.com/shareAI-lab/learn-claude-code/commit/ce8f9f186058939da54c9d6fead78dfb5d0fd6c3) as the source baseline. This repository adds learning notes, local exercises, and setup documentation, and preserves local modifications to the first chapter.

Distributed under the [MIT License](LICENSE). Original copyright: Copyright (c) 2024 shareAI Lab. Retain the original copyright and license notice when redistributing.
