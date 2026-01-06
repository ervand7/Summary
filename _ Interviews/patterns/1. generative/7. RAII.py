# RAII — Resource Acquisition Is Initialization
# ❓ The idea
# A resource is acquired when an object is created and released when the object
# is destroyed.
# So lifetime of the object = lifetime of the resource.

class File:
    def __init__(self, path: str):
        self.file = open(path, "w")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()


# Usage
with File("data.txt") as f:
    f.write("hello")
# file is closed automatically here
