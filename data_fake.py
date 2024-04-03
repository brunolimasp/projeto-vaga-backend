from random import choice
from faker import Faker
from src.config.database import db

# Crie uma instância do Faker
fake = Faker()

# Dados do Faker para tabela departments
departments = {
    1: "Marketing",
    2: "Desenvolvimento",
    3: "Recursos Humanos",
    4: "Vendas",
    5: "Suporte Técnico",
    6: "Financeiro",
    7: "Produção",
    8: "Engenharia",
    9: "Atendimento ao Cliente",
    10: "Administração",
}


def data_fake(departments):
    try:
        for department_id, department_name in departments.items():
            db.execute(
                f"INSERT INTO public.departments (id, department) VALUES ({department_id}, '{department_name}')"
            )

        # Dados do Faker para tabela employees
        for employees in range(0, 50):
            fake_name = fake.name()
            random_department = choice(list(departments.keys()))
            have_dependents = choice([True, False])
            db.execute(
                f"INSERT INTO public.employees (full_name, department, have_dependents) VALUES ('{fake_name}',{random_department}, {have_dependents});"
            )
    except:
        pass


data_fake(departments)
