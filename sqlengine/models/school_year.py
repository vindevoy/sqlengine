from datetime import date

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.models.base import Base


class SchoolYear(Base):
    """
    SchoolYear demo class

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __tablename__ = "tbl_school_years"

    name: Mapped[str] = mapped_column(String(10))
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"SchoolYear(id={self.id}, name={self.name})"
