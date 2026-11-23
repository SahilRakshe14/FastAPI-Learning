
from pydantic import BaseModel , Field , EmailStr , field_validator

"""
FINAL STUDENT MODEL
field_validator -> our own custom rule
"""

class student(BaseModel):
    id     : str = Field(..., json_schema_extra={"example": "S001"})
    name   : str = Field(..., min_length = 2 , max_length = 150)
    age    : int = Field(..., gt = 0 , le = 100)
    course : str = Field(..., max_length = 50)
    marks  : int = Field(..., ge = 0 , le = 100)
    email  : EmailStr

    # Custom Rule : Name must contain only letters and spaces
    
    @field_validator("name")     # name = sahil rakshe
    @classmethod
    def check_name(cls , value):     # value = "sahil rakshe"
        if not value.replace(" ", "").isalpha():
            raise ValueError("name must contain only letters and spaces")

        return value.title()   # Sahil Rakshe

S = student(id = "S001" ,
                name= "sahil rakshe",
                age = 21,
                course = "Python",
                marks = 90,
                email = "sahilrakshe70@gmail.com"
                )

print(S.id)
print(S.name)
print(S.age)
print(S.course)
print(S.marks) 
print(S.email)
