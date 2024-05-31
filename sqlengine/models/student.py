from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.models.base import Base


class Student(Base):
    """
    Student demo class

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_students"

    login: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"Student(id={self.id}, login={self.login}, name={self.first_name} {self.last_name})"
