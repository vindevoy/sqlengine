from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.models.base import Base

if TYPE_CHECKING:
    from sqlengine.models.registration import Registration
    from sqlengine.models.subject import Subject


class Grade(Base):
    """
    Grade demo class

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_grades"

    registration_id: Mapped[int] = mapped_column(ForeignKey("tbl_registrations.id"))
    registration: Mapped["Registration"] = relationship(back_populates="grades")

    subject_id: Mapped[int] = mapped_column(ForeignKey("tbl_subjects.id"))
    subject: Mapped["Subject"] = relationship(back_populates="grades")

    score: Mapped[int] = mapped_column(Integer)
    min_score: Mapped[int] = mapped_column(Integer)
    max_score: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        # TODO: better repr with details on the student, ...
        return f"Grade(id={self.id}, registration={self.registration}"
