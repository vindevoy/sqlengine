from typing import List, TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.common.base import Base

if TYPE_CHECKING:
    from sqlengine.samples.registration import Registration
    from sqlengine.samples.subject import Subject


class Course(Base):
    """
    Course demo class

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_courses"

    mnemonic: Mapped[str] = mapped_column(String(10))
    name: Mapped[str] = mapped_column(String(50))

    subjects: Mapped[List["Subject"]] = relationship(
        "Subject",
        back_populates="course",
        cascade="all, delete-orphan")

    registrations: Mapped[List["Registration"]] = relationship(
        "Registration",
        back_populates="course",
        cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"Course(id={self.id}, mnemonic={self.mnemonic}, name={self.name})"
