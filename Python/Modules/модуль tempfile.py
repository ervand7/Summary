# официальная документация: https://docs.python.org/3/library/tempfile.html
import tempfile

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')

# get file size
print(fp.tell())  # 12

# read data from file
fp.seek(0)
print(fp.read())  # b'Hello world!'

# close the file, it will be removed
fp.close()

# ________________________________________________________________
# create a temporary file using a context manager
with tempfile.TemporaryFile() as f:
    f.write(b'Hello world!')
    f.seek(0)
    print(f.read())  # b'Hello world!'

# file is now closed and removed

# ________________________________________________________________
# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    # created temporary directory /var/folders/tx/zk1hwqdd78vbld5zx2s862f00000gn/T/tmp1dso89sw

# directory and contents have been removed
