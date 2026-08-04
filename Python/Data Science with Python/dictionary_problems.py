# # 🟣 Dictionary (15 Problems)

# 36. Create a dictionary of student details.
student_details = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.8
}
# 37. Print all keys of a dictionary.
for key in student_details.keys():
    print(f"Key: {key}")
# 38. Print all values of a dictionary.
for value in student_details.values():
    print(f"Value: {value}")
# 39. Print all key-value pairs.
for key, value in student_details.items():
    print(f"Key: {key}, Value: {value}")
# 40. Add a new key-value pair.
student_details["email"] = "john.doe@example.com"
# 41. Update the value of an existing key.
student_details["GPA"] = 3.9
# 42. Delete a key from the dictionary.
del student_details["age"]
# 43. Check whether a key exists.
key_to_check = "major"
if key_to_check in student_details:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
# 44. Count the number of key-value pairs.
num_pairs = len(student_details)
print(f"Number of key-value pairs: {num_pairs}")
# 45. Find the student with the highest marks.
highest_student = max(student_details, key=lambda x: student_details[x]["GPA"])
print(f"Student with the highest marks: {highest_student}")
# 46. Calculate the sum of all values in a dictionary.
total_gpa = sum(student_details[key]["GPA"] for key in student_details if "GPA" in student_details[key])
print(f"Total GPA: {total_gpa}")
# 47. Merge two dictionaries.
stud1 = {"name": "Alice", "age": 22}
stud2 = {"major": "Mathematics", "GPA": 3.7}

students = {**stud1, **stud2}
print(f"Merged dictionary: {students}")
         
# 48. Create a dictionary from two lists (keys and values).
keys = ["name", "age", "major"]
values = ["Bob", 21, "Physics"]
student_info = dict(zip(keys, values))
print(f"Dictionary from two lists: {student_info}")
# 49. Count the frequency of each character in a string using a dictionary.
text = "hello world"
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1
print(f"Character frequency: {char_freq}")
# 50. Count the frequency of each word in a sentence using a dictionary.
sentence = "hello world hello"
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print(f"Word frequency: {word_freq}")

