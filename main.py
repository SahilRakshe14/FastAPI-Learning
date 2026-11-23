from fastapi import FastAPI

from Basic_Routes.main import router as basic_router
from Path_Parameters.student import router as student_router
from Query_Parameters.filter import router as filter_router
from Sorting.sorting import router as sorting_router
from Pagination.paginate import router as paginate_router


app = FastAPI(
    title="Sahil's FastAPI Learning Project",
    description="Learning FastAPI with different API concepts",
    version="1.0.0"
)


# Register all routers.
app.include_router(basic_router)
app.include_router(student_router)
app.include_router(filter_router)
app.include_router(sorting_router)
app.include_router(paginate_router)