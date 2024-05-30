from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.common.session_factory import SessionFactory


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def create(self):
        with SessionFactory.get_session() as session:
            session.add(self)
            session.commit()

    @classmethod
    def read(cls, rec_id: int):
        with SessionFactory.get_session() as session:
            record = session.get(cls, rec_id)

            return record
