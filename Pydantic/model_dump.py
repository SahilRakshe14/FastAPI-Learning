
from pydantic import BaseModel, Field, EmailStr, field_validator, computed_field

"""
Model_Dump()
Turn a model back into Python dictionary(so that we can save it later)
"""


class student(BaseModel):
    id: str = Field(..., examples=["S001"])
    name: str = Field(..., min_length=2, max_length=150)
    age: int = Field(..., gt=0, le=100)
    course: str = Field(..., max_length=50)
    marks: int = Field(..., ge=0, le=100)
    email: EmailStr

    # Custom Rule: Name must contain only letters and spaces

    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("name must contain only letters and spaces")

        return value.title()

    @computed_field
    @property
    def grade(self) -> str:
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"


S = student(
    id="S001",
    name="sahil rakshe",
    age=21,
    course="Python",
    marks=90,
    email="sahilrakshe70@gmail.com"
)

print(S.id)
print(S.name)
print(S.age)
print(S.course)
print(S.marks)
print(S.email)
print(S.grade)

data = S.model_dump()
print(data)
