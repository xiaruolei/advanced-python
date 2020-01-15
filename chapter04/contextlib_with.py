import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("enter")
    yield {}
    print("exit")


with file_open("file") as f:
    print("processing")