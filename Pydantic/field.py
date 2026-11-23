"""
FIELD() RULES

gt = grether than                    lt = less than
ge = grethar or equal                le = less or equal
"""

from pydantic import BaseModel , Field

class RuleStudent(BaseModel):
    name   : str = Field(..., min_length = 2 , max_length = 50)  # ... = requird
    age    : int = Field(..., gt = 0 , lt = 100)                 # 1 to 99
    marks  : int = Field(..., gt = 0 , lt = 100)                 #0 to 100
    course : str = "Python"                                      #default value -> python
    phone  : str |  None = None                                 #Optional Field can be Empty
R = RuleStudent(name = "Sahil rakshe" , age = 21 , marks = 90)

print(R.name)
print(R.age)
print(R.marks)
print(R.course)
print(R.phone)
