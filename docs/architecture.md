# env-gen Architecture and Software Design

This document describes the architecture and software design for the env-gen project, following the Platform Bootstrap + Python Core approach.

## Overview

- Platform-specific bootstrap scripts ensure Python is available, then delegate to Python for all logic.
- Python modules handle environment checks, tool installation, user prompts, and VS Code config generation.
- Templates are used for generating configuration files.

## Directory Structure

```text
/ (project root)
│
├── scripts/                # Platform-specific bootstrap scripts
│   ├── bootstrap.sh        # macOS/Linux bootstrap
│   └── bootstrap.bat       # Windows bootstrap
│
├── envgen/                 # Python core logic
│   ├── __init__.py
│   ├── cli.py              # Main CLI entrypoint
│   ├── platform.py         # Platform detection/abstraction
│   ├── checks.py           # Environment/tool checks
│   ├── install.py          # Tool installation logic
│   └── vscode.py           # VS Code config generation
│
├── templates/              # VS Code and other config templates
│
├── docs/                   # Documentation
│
├── README.md
└── ...
```

## Module Responsibilities

- **scripts/bootstrap.sh, bootstrap.bat**: Check/install Python, then call `python -m envgen.cli`.
- **envgen/cli.py**: Main CLI, handles argument parsing and user prompts.
- **envgen/platform.py**: Detects OS/platform, abstracts platform-specific logic.
- **envgen/checks.py**: Checks for compilers, debuggers, Python, etc.
- **envgen/install.py**: Installs missing tools using system package managers.
- **envgen/vscode.py**: Generates VS Code config files from templates.

## Flow Diagram

1. User runs `scripts/bootstrap.sh` or `scripts/bootstrap.bat`.
2. Script ensures Python is installed, then runs `python -m envgen.cli`.
3. CLI checks environment, prompts user for choices, installs tools if needed.
4. Generates VS Code workspace/config files using templates.

## Extensibility

- Add new platforms by extending `platform.py` and adding new bootstrap scripts.
- Add new environment checks or installers in `checks.py` and `install.py`.
- Add new templates for different project types in `templates/`.

---

For more details, see the individual module docs or source code.
