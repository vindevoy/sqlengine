from typing import TYPE_CHECKING, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.common.base import Base

if TYPE_CHECKING:
    from sqlengine.samples.course import Course
    from sqlengine.samples.grade import Grade


class Subject(Base):
    """
    Subject demo class

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_subjects"

    mnemonic: Mapped[str] = mapped_column(String(15))
    name: Mapped[str] = mapped_column(String(50))

    course_id: Mapped[int] = mapped_column(ForeignKey("tbl_courses.id"))
    course: Mapped["Course"] = relationship(back_populates="subjects")

    grades: Mapped[List["Grade"]] = relationship(
        "Grade",
        back_populates="subject",
        cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"Subject(id={self.id}, mnemonic={self.mnemonic}, name={self.name})"
