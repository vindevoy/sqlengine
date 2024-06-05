from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.models.base import Base


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

    def __repr__(self) -> str:
        """
        default __repr__ method.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return f"Course(id={self.id}, mnemonic={self.mnemonic}, name={self.name})"
