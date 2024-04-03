from fastapi import APIRouter

from .endpoints import get_list

department_router = APIRouter()

department_router.include_router(get_list.router)
