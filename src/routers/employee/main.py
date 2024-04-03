from fastapi import APIRouter

from .endpoints import get_list

employee_router = APIRouter()

employee_router.include_router(get_list.router)
