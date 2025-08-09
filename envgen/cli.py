"""
Main CLI entrypoint for envgen.
"""
def main():

import argparse
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from . import checks
from . import vscode

def main():
    parser = argparse.ArgumentParser(
        description="env-gen: Environment generator for C/C++ and autoconf projects."
    )
    parser.add_argument('--check', action='store_true', help='Check environment and required tools')
    parser.add_argument('--generate', action='store_true', help='Generate VS Code configuration files')
    parser.add_argument('--target', type=str, default=os.getcwd(), help='Target directory for config generation')
    args = parser.parse_args()

    console = Console()

    if args.check:
        console.print(Panel("[bold cyan]Checking environment...[/bold cyan]", title="envgen"))
        results = checks.check_all()
        table = Table(title="Tool Check Results", show_header=True, header_style="bold magenta")
        table.add_column("Tool", style="dim")
        table.add_column("Status", style="bold")
        for tool, present in results.items():
            status = "[green]FOUND[/green]" if present else "[red]MISSING[/red]"
            table.add_row(tool, status)
        console.print(table)
    if args.generate:
        console.print(Panel(f"[bold green]Generating VS Code configuration in {args.target}...[/bold green]", title="envgen"))
        vscode.generate_vscode_configs(args.target)
    if not (args.check or args.generate):
        parser.print_help()


if __name__ == "__main__":
    main()
