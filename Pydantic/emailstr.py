"""
EMAILSTR
check the txt really looks like an email
"""

from pydantic import BaseModel , Field , EmailStr


class EmailStudent(BaseModel):
      name  : str
      email : EmailStr

S = EmailStudent(name = 'Sahil Rakshe' , email = 'sahlrakshe70@gmail.com')

print(S.name)
print(S.email)
