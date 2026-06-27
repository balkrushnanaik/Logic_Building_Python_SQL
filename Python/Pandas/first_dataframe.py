# ### 1.
# Create a DataFrame named `students` with columns:
# * student_id
# * name
# * age
# * marks


import pandas as pd

data = {
    "Student_id":[1,2,3,4],
    "name":['k','S','D','V'],
    "age":[22,23,24,25],
    "marks":[99,89,87,67]

}
students = pd.DataFrame(data)
print(students)

students.info()
students.shape()