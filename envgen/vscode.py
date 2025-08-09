"""
VS Code configuration file generation for envgen.
"""
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), '..', 'templates')


def generate_vscode_configs(target_dir):
    """Stub: Generate VS Code config files in the target directory."""
    # TODO: Implement template rendering and file writing
    print(f"[envgen] Would generate VS Code configs in {target_dir}")
