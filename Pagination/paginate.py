"""
PAGINATION 

http://127.0.0.1:8000/paginate?page=1&limit=2

page -> Which page you want
limet -> How many students records on one page

formula:
start = page -1 * limit
end = start + limit
"""  

import json
from fastapi import APIRouter, HTTPException, Path

router = APIRouter(tags=["paginate"])

from Data_Handling.data import load_data

@router.get("/Paginate")
def paginate_student(page : int , limit : int):
    data = load_data()

    # Turn the disctionary into a list, Putting Id inside each student

    student = []
    for student_id , info in data.items():
        info["id"] = student_id
        student.append(info)

    start = (page - 1) * limit
    end = start + limit

    page_student = student[start : end]
    total_student = len(student)

    return{
        "page" : page,
        "limit" : limit,
        "total_student" : total_student,
        "student" : page_student
    }

