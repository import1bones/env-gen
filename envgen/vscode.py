"""
VS Code configuration file generation for envgen.
"""
def generate_vscode_configs(target_dir):
import os
import shutil

TEMPLATES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

def generate_vscode_configs(target_dir):
    """Copy template VS Code config files to the target directory's .vscode folder."""
    vscode_dir = os.path.join(target_dir, '.vscode')
    os.makedirs(vscode_dir, exist_ok=True)
    for fname in ['tasks.json', 'launch.json']:
        src = os.path.join(TEMPLATES_DIR, fname)
        dst = os.path.join(vscode_dir, fname)
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            print(f"[envgen] Generated {dst}")
        else:
            print(f"[envgen] Template {fname} not found in {TEMPLATES_DIR}")
