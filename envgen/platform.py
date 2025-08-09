"""
Platform detection and abstraction for envgen.
"""

import sys

def get_platform():
    
    """Return a string representing the current platform."""
    plt = sys.platform
    if plt.startswith('linux'):
        return 'linux'
    elif plt == 'darwin':
        return 'macos'
    elif plt in ('win32', 'cygwin'):
        return 'windows'
    else:
        return 'unknown'

    
def is_supported():
    """Return True if the platform is supported."""
    return get_platform() in ('linux', 'macos', 'windows')
