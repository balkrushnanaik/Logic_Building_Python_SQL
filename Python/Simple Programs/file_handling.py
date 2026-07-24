# ### 8. File Handling (97–98)

# 97. Write text to a file.
with open('test.txt', 'w') as f:
    f.write("Hello, this is a test file.\n")
    f.write("This file is created for testing purposes.\n")
    f.write("File handling in Python is easy and fun!\n")

# 98. Read text from a file.
