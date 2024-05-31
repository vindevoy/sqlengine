from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.common.session_factory import SessionFactory
from sqlengine.common.transaction_factory import TransactionFactory


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def create(self):
        with TransactionFactory.get_transaction() as transaction:
            transaction.create(self)

    @classmethod
    def read(cls, rec_id: int):
        with TransactionFactory.get_transaction() as transaction:
            return transaction.read(cls, [rec_id])[0]

    def update(self):
        with TransactionFactory.get_transaction() as transaction:
            transaction.update(self)

    def delete(self):
        with TransactionFactory.get_transaction() as transaction:
            transaction.delete(self)

    @classmethod
    def record_count(cls):
        with SessionFactory.get_session() as session:
            rec_count = session.query(func.count(cls.id)).scalar()

            return rec_count
