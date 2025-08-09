"""
Environment and tool checks for envgen.
"""
import shutil

REQUIRED_TOOLS = [
    'gcc',
    'g++',
    'make',
    'python3',
]


def check_tool(tool):
    """Return True if the tool is found in PATH."""
    return shutil.which(tool) is not None


def check_all():
    """Check all required tools and return a dict of results."""
    results = {}
    for tool in REQUIRED_TOOLS:
        results[tool] = check_tool(tool)
    return results
