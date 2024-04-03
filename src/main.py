from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from src.routers.department.main import department_router
from src.routers.employee.main import employee_router

load_dotenv()
app = FastAPI()


# -------------------Configurção da documentação openapi swagger/redoc-------------
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="ACMEVita - backend-datasets",
        version="1.0",
        summary="APIs para acessar dados do banco de dados PostgreSQL",
        description="Este conjunto de APIs fornece acesso aos dados armazenados no banco de dados PostgreSQL da ACMEVita.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
# --------------------------------Configurção de CORS--------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------Inclusão das rotas--------------------------------
app.include_router(department_router, prefix="/department", tags=["department"])
app.include_router(employee_router, prefix="/employee", tags=["employee"])
