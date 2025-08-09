# Quick Start Example for Beginners

This example will help you quickly set up a C/C++ development environment in VS Code using env-gen.

## 1. Clone the Repository


```sh
git clone https://github.com/import1bones/env-gen.git
cd env-gen
```

## 2. Run the Bootstrap Script

- **macOS/Linux:**

  ```sh
  ./scripts/bootstrap.sh --check --generate --target my-cpp-project
  ```

- **Windows:**

  ```bat
  scripts\bootstrap.bat --check --generate --target my-cpp-project
  ```

## 3. Open in VS Code


```sh
code my-cpp-project
```

## 4. Add Your Source Code

Place your `.c` or `.cpp` files in `my-cpp-project` and use the pre-configured build and debug tasks.

---

This will:

- Check for required tools (and help you install them if missing)
- Generate `.vscode/tasks.json` and `.vscode/launch.json` for you
- Let you build and debug C/C++ code in VS Code immediately
