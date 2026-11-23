
from fastapi import APIRouter, HTTPException, Query

router = APIRouter(tags=["Sorting"])

#common function
from Data_Handling.data import load_data


# Sort students using query parameters.
# Example: /students/sort?sort_by=salary&order=asc
@router.get("/students/sort")
def sort_students(

    # Field to sort: marks or salary.
    sort_by: str = Query("marks", description="Field used for sorting"),

    # Sorting order: asc or desc.
    order: str = Query("asc", description="Sorting order")
):

    # Load all student records.
    data = load_data()

    # Convert student dictionary into a list.
    students = []

    for student_id, info in data.items():

        # Copy student details and add student ID.
        student = {
            **info,
            "id": student_id
        }

        students.append(student)

    # Validate sorting field.
    if sort_by not in ["marks", "salary"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort_by field. Use marks or salary."
        )

    # Validate sorting order.
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Use asc or desc."
        )

    # True = Descending, False = Ascending.
    reverse = (order == "desc")

    # Sort students using lambda and sorted().
    sorted_student = sorted(
        students,
        key=lambda s: s[sort_by],
        reverse=reverse
    )

    # Return sorted student records.
    return sorted_student
