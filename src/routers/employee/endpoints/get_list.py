from fastapi import APIRouter, Depends, Query

from src.config.database import db

router = APIRouter()


def builder_query_string(department: str = None) -> str:
    # Constroi a query SQL
    return f"""SELECT e.full_name AS full_name,
                        e.have_dependents AS have_dependents,
                        d.department AS department
                        FROM public.employees e LEFT JOIN public.departments d ON d.id = e.department WHERE d.department = '{department}';"""


dp = [
    "Marketing",
    "Desenvolvimento",
    "Recursos Humanos",
    "Vendas",
    "Suporte Técnico",
    "Financeiro",
    "Produção",
    "Engenharia",
    "Atendimento ao Cliente",
    "Administração",
]


@router.get("/list")
async def get_employees_list(department: str = Query(dp[0], enum=dp)):
    """
    Lista os funcionários de um departamento específico.

    - **department**: Nome do departamento a ser listado.
    """

    sql_query = builder_query_string(department)
    return db.execute(sql_query)
