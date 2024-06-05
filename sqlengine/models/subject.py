from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.models.base import Base

if TYPE_CHECKING:
    from sqlengine.models.course import Course


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

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"Subject(id={self.id}, mnemonic={self.mnemonic}, name={self.name})"
