"""
Tool installation logic for envgen.
"""

import subprocess
from .platform import get_platform


def install_tool(tool):
    
    """Attempt to install the given tool using the system package manager."""
    platform = get_platform()
    if platform == 'macos':
        subprocess.run(['brew', 'install', tool], check=False)
    elif platform == 'linux':
        subprocess.run(['sudo', 'apt-get', 'install', '-y', tool], check=False)
    elif platform == 'windows':
        # Prefer winget if available, fallback to choco
        from shutil import which
        if which('winget'):
            subprocess.run([
                'winget', 'install', '--id', tool, '-e', '--silent'
            ], check=False)
        elif which('choco'):
            subprocess.run(['choco', 'install', tool, '-y'], check=False)
        else:
            msg = (f"[envgen] Neither winget nor choco found. "
                   f"Please install {tool} manually.")
            print(msg)
    else:
        print(f"[envgen] Unsupported platform for installing {tool}.")
