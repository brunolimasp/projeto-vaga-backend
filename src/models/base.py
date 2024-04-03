from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

# 2. Crie uma instância de declarative_base
Base = declarative_base()


class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    department = Column(String)


class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    department = Column(Integer)
    have_dependents = Column(Boolean)
