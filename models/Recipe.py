from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Float, Date, ForeignKey
from typing import List
from datetime import date


class CategoryExpense(Base):
    __tablename__ = 'categories_expenses'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    nome:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    despesas: Mapped[List['Expense']] = relationship('Expense', backref='categoria', lazy=True)



class Recipe(Base):
    __tablename__ = "recipes"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    descricao:Mapped[str] = mapped_column(String(100), nullable=False)
    valor:Mapped[float] = mapped_column(Float, nullable=False)
    data:Mapped[date] = mapped_column(Date, nullable=False)


class Expense(Base):
    __tablename__ = "expenses"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    descricao:Mapped[str] = mapped_column(String(100), nullable=False)
    valor:Mapped[float] = mapped_column(Float, nullable=False)
    data:Mapped[date] = mapped_column(Date, nullable=False)
    categoria_id:Mapped[int] = mapped_column(Integer, ForeignKey('categories_expenses.id'), nullable=False)
