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

    def update(self):
        with SessionFactory.get_session() as session:
            current = session.get(self.__class__, self.id)

            column_names = self.__class__.__table__.columns.keys()

            for column in column_names:
                if column != "id":
                    setattr(current, column, getattr(self, column))

            session.commit()
