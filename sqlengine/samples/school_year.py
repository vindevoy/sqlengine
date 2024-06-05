from datetime import date
from typing import List, TYPE_CHECKING

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from sqlengine.common.base import Base

if TYPE_CHECKING:
    from sqlengine.samples.registration import Registration


class SchoolYear(Base):
    """
    SchoolYear demo class

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_school_years"

    description: Mapped[str] = mapped_column(String(10))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)

    registrations: Mapped[List["Registration"]] = relationship(
        "Registration",
        back_populates="school_year",
        cascade="all, delete-orphan")

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"SchoolYear(id={self.id}, description={self.description})"
