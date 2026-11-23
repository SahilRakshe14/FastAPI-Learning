# Import required modules.
import json
from fastapi import APIRouter, HTTPException, Path

router = APIRouter(tags=["Path Parameters"])


# Load student data from JSON file.
from Data_Handling.data import load_data


# Get all student records.
# Example: /student
@router.get("/student")
def student():
    return load_data()


# Get a specific student using path parameter.
# Example: /student/101
@router.get("/student/{student_id}")
def get_student(student_id: str):

    # Load all student records.
    data = load_data()

    # Check whether the student ID exists.
    if student_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student ID '{student_id}' does not exist!"
        )

    # Return the requested student's details.
    return data[student_id]