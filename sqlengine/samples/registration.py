from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.common.base import Base

if TYPE_CHECKING:
    from sqlengine.samples.course import Course
    from sqlengine.samples.grade import Grade
    from sqlengine.samples.school_year import SchoolYear
    from sqlengine.samples.student import Student


class Registration(Base):
    """
    Registration demo class

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_registrations"

    student_id: Mapped[int] = mapped_column(ForeignKey("tbl_students.id"))
    student: Mapped["Student"] = relationship(back_populates="registrations")

    course_id: Mapped[int] = mapped_column(ForeignKey("tbl_courses.id"))
    course: Mapped["Course"] = relationship(back_populates="registrations")

    school_year_id: Mapped[int] = mapped_column(ForeignKey("tbl_school_years.id"))
    school_year: Mapped["SchoolYear"] = relationship(back_populates="registrations")

    grades: Mapped[List["Grade"]] = relationship(
        "Grade",
        back_populates="registration",
        cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return (f"Registration(id={self.id}, school year={self.school_year.description}, "
                f"student={self.student.first_name} {self.student.first_name}, "
                f"course={self.course.name})")
