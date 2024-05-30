from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.models.base import Base


class Student(Base):
    __tablename__ = "tbl_students"

    login: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"Student(id={self.id}, login={self.login}, name={self.first_name} {self.last_name})"
