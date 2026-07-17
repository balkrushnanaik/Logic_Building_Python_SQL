import os

# Simple program to check whether a file or directory named 'anyone' exists
# in the current working directory.
name = "anyone"
path = os.path.join(os.getcwd(), name)

if os.path.exists(path):
    print(f"'{name}' is available in the current folder: {path}")
else:
    print(f"'{name}' is not available in the current folder: {os.getcwd()}")
