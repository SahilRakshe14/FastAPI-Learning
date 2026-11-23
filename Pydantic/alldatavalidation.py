from model_dump import student as Student
import json

"""
Step 7 - CHECK OUR REAL DATA (students.json)
Every student in our file will go through the Student Model
"""

with open("student.json", "r") as file:
    raw = json.load(file)

for student_id, info in raw.items():
    s = Student(id=student_id, **info)
    print(s.id, s.name, s.grade)