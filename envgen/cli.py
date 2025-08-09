"""
Main CLI entrypoint for envgen.
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="env-gen: Environment generator for C/C++ and autoconf projects.")
    parser.add_argument('--check', action='store_true', help='Check environment and required tools')
    parser.add_argument('--generate', action='store_true', help='Generate VS Code configuration files')
    args = parser.parse_args()

    if args.check:
        print("[envgen] Checking environment...")
        # TODO: Call checks module
    if args.generate:
        print("[envgen] Generating VS Code configuration...")
        # TODO: Call vscode module
    if not (args.check or args.generate):
        parser.print_help()

if __name__ == "__main__":
    main()
