from fastapi import APIRouter

from src.config.database import db

router = APIRouter()


@router.get("/list")
async def get_departments_list():
    """
    Lista os departamentos da empresa.

    """
    sql_query = "SELECT department FROM public.departments"
    return db.execute(sql_query)
