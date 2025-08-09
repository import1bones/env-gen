"""
Main CLI entrypoint for envgen.
"""
import argparse
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from . import checks
from . import vscode


def main():
    parser = argparse.ArgumentParser(
        description="env-gen: Environment generator for C/C++ projects."
    )
    parser.add_argument(
        '--check', action='store_true',
        help='Check environment and required tools'
    )
    parser.add_argument(
        '--generate', action='store_true',
        help='Generate VS Code configuration files'
    )
    parser.add_argument(
        '--target', type=str, default=os.getcwd(),
        help='Target directory for config generation'
    )
    parser.add_argument(
        '--non-interactive', action='store_true',
        help='Run in non-interactive mode (skip tool installation prompts)'
    )
    args = parser.parse_args()

    console = Console()

    if args.check:
        console.print(Panel(
            "[bold cyan]Checking environment...[/bold cyan]",
            title="envgen"
        ))
        results = checks.check_all()
        table = Table(
            title="Tool Check Results",
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Tool", style="dim")
        table.add_column("Status", style="bold")
        missing_tools = []
        for tool, present in results.items():
            status = ("[green]FOUND[/green]" if present
                      else "[red]MISSING[/red]")
            table.add_row(tool, status)
            if not present:
                missing_tools.append(tool)
        console.print(table)
        if missing_tools:
            missing_str = ', '.join(missing_tools)
            console.print(Panel(
                f"[yellow]Missing tools: {missing_str}[/yellow]",
                title="envgen"
            ))
            if not args.non_interactive:
                from rich.prompt import Confirm
                from .install import install_tool
                for tool in missing_tools:
                    prompt = f"Install [bold]{tool}[/bold]?"
                    if Confirm.ask(prompt, default=True):
                        install_tool(tool)
                    else:
                        msg = (f"[yellow]Skipped installation of "
                               f"{tool}.[/yellow]")
                        console.print(msg)
            else:
                msg = ("[yellow]Non-interactive mode: skipping tool "
                       "installation.[/yellow]")
                console.print(msg)
    if args.generate:
        gen_msg = (f"[bold green]Generating VS Code configuration "
                   f"in {args.target}...[/bold green]")
        console.print(Panel(gen_msg, title="envgen"))
        vscode.generate_vscode_configs(args.target)
    if not (args.check or args.generate):
        parser.print_help()


if __name__ == "__main__":
    main()
