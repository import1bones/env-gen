"""
Tool installation logic for envgen.
"""
import subprocess
import sys
from .platform import get_platform

def install_tool(tool):
    """Attempt to install the given tool using the system package manager."""
    platform = get_platform()
    if platform == 'macos':
        subprocess.run(['brew', 'install', tool], check=False)
    elif platform == 'linux':
        subprocess.run(['sudo', 'apt-get', 'install', '-y', tool], check=False)
    elif platform == 'windows':
        subprocess.run(['choco', 'install', tool, '-y'], check=False)
    else:
        print(f"[envgen] Unsupported platform for installing {tool}.")
