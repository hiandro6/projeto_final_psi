from sqlalchemy.orm import mapped_column, relationship, Mapped


from typing import List
from database import Base
from flask_login import UserMixin
from database.config import session

class User(Base, UserMixin):
    __tablename__ = 'tb_users'
    usr_id:Mapped[int] = mapped_column(primary_key = True, autoincrement=True)
    usr_nome:Mapped[str] = mapped_column(nullable=False)
    usr_email:Mapped[str] = mapped_column(unique = True, nullable=False)
    usr_senha:Mapped[str] = mapped_column(unique = True, nullable=False)
    # despesas: Mapped[list["Despesa"]] = relationship("Despesa", back_populates="user", cascade="all, delete-orphan")
    
    @classmethod
    def find(cls, **kwargs):
        if 'email' in kwargs:
            return session.query(cls).filter_by(cli_email=kwargs['email']).first() 
        elif 'id' in kwargs:
            return session.query(cls).filter_by(cli_id=kwargs['id']).first()
        else: 
            raise AttributeError('A busca deve ser feita por email ou id.')