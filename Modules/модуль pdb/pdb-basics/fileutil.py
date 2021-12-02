def get_path(fname):
    """Return file's path or empty string if no path."""
    import os
    breakpoint()
    head, tail = os.path.split(fname)
    return head
