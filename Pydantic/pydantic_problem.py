"""
PYDANTIC FUNDAMENTALS

install pydantic : pip install pydantic
"""

"""
STEP 1 - The Problem
A normal discinory accept ANYTHING. nobody check data
"""
bad_student = {
    "name"  : "",
    "age"   : "Twenty one",
    "marks" : 152,
    "email" :"Not-an-email"
}

# print(bad_student)



from pydantic import BaseModel
"""
STEP 2 - BASEMODEL + TYPE HINTS
We describe a student ONCE. Python checks every student student aginst it
"""

class simpleStudent(BaseModel):
    name : str
    age : int
    marks : int

S = simpleStudent(name = "Sahil Rakshe" , age = "21" , marks = "86")
print(S.name ,S.age, S.marks)