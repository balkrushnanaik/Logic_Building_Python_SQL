# File Handling in Python: 

# File handling is a crucial aspect of programming that allows you to read from and write to files on your computer's file system.
# Python provides built-in functions and methods to work with files, making it easy to perform various operations such as reading, writing, appending, and closing files.
# Files can be opened in different modes, such as read mode ('r'), write mode ('w'), append mode ('a'), and binary mode ('b'). Each mode serves a specific purpose and determines how the file will be accessed.
# When working with files, it's important to handle exceptions that may occur, such as file not found errors or permission errors. Using try-except blocks can help manage these exceptions gracefully.

# try:
#     with open("file.txt", "w") as file:
#         file.write("Hello, World!")
#         file.write("\nThis is a sample file for file handling in Python.")
#         file.write("\nYou can read from and write to files using Python's built-in functions.")
# except Exception as e:
#     print(f"An error occurred while writing to the file: {e}")
# else:
#     print("File written successfully.")
# finally:
#     print("File handling operation completed.")

# With the 'with' statement, the file is automatically closed after the block of code is executed, ensuring proper resource management.

with open("file.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
