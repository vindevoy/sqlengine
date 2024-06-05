from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.common.base import Base

if TYPE_CHECKING:
    from sqlengine.models.registration import Registration


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

    registrations: Mapped[List["Registration"]] = relationship(
        "Registration",
        back_populates="student",
        cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"Student(id={self.id}, login={self.login}, name={self.first_name} {self.last_name})"
