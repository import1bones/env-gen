# env-gen

env-gen is a cross-platform environment generator for C/C++ and GNU autoconf-based projects, designed to help both beginners and advanced users set up and manage their development environments in VS Code.

## What does env-gen do?

- Provides platform-specific scripts to install Python (if missing) and then uses Python for all further automation.
- Checks for required tools (compilers, debuggers, etc.) and can handle their installation.
- Supports all major platforms (macOS, Linux, Windows).
- Generates VS Code configuration files (tasks.json, launch.json, etc.) for your project.
- Prompts users interactively to choose and generate new environments or templates.

## How to use

1. Run the platform-specific script to ensure Python is available.
2. Use the provided Python scripts to check your environment and generate VS Code workspace files.
3. Follow the interactive prompts to select the environment or template you want.


## 🚀 Quick Start for Beginners

👉 **See the [Beginner Quick Start Example](docs/quickstart-beginner.md) for the fastest way to set up your C/C++ environment in VS Code!**

## Documentation

See the [docs/](docs/README.md) folder for detailed documentation, including:

- Overview
- Getting Started
- Platform Scripts
- VS Code Integration
- Templates & Advanced Usage

## Who is this for?

- **Beginners:** Easily generate a new development environment for C/C++ projects in VS Code.
- **Advanced users:** Use templates and automation to quickly set up or replicate environments.

---

For more details, see the [docs/](docs/README.md) folder.
