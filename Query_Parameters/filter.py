# Import required modules.
import json
from fastapi import APIRouter, Query

router = APIRouter(tags=["Query Parameters"])


# Example: /filter?course=Python

# Load student data from JSON file.
from Data_Handling.data import load_data


# Filter students using query parameters.
@router.get("/filter")
def filter_student(

    # Optional query parameter to filter by course.
    course: str = Query(
        None,
        description="Show only students in course",
        examples=["Python"]
    )
):

    # Load all student records.
    data = load_data()

    # Return all students if no course is provided.
    if course is None:
        return data

    # Store students matching the requested course.
    filtered = {}

    # Iterate through student ID and information.
    for student_id, info in data.items():

        # Compare courses without case sensitivity.
        if info["course"].lower() == course.lower():

            # Add matching student to the filtered dictionary.
            filtered[student_id] = info

    # Return filtered student records.
    return filtered