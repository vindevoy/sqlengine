from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlengine.common.session_factory import SessionFactory
from sqlengine.common.transaction_factory import TransactionFactory


class Base(DeclarativeBase):
    """
    Base declarative model off which all other models will inherit from.
    This class has also several methods used in all models that inherit from Base.
    Most of these methods will forward the work to the transaction classes.

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    ###
    # id is a common field for all records.  This engine follows the principles of Django where each record has
    # its own id, automatically generated when the record is created.
    id: Mapped[int] = mapped_column(primary_key=True)
    ###

    def create(self) -> None:
        """
        Create a new record in the database.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        with TransactionFactory.get_transaction() as transaction:
            transaction.create(self)

    @classmethod
    def read(cls, rec_id: int) -> Any:
        """
        Read a record in the database by its id.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        with TransactionFactory.get_transaction() as transaction:
            return transaction.read(cls, [rec_id])[0]

    def update(self) -> None:
        """
        Update the record in the database.  The record is first read, the all properties are passed.
        Finally, the updated record is written to the database.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        with TransactionFactory.get_transaction() as transaction:
            transaction.update(self)

    def delete(self) -> None:
        """
        Delete the record in the database.  The record must first be read, or at least by available in the session,
        before it can be deleted.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        with TransactionFactory.get_transaction() as transaction:
            transaction.delete(self)

    @classmethod
    def record_count(cls) -> int:
        """
        Return the record count for a table in the database.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        ###
        # Method is here and not in transaction as I don't see a reason to get multiple record counts at once.
        ###

        with SessionFactory.get_session() as session:
            rec_count = session.query(func.count(cls.id)).scalar()

            return rec_count

    @classmethod
    def all(cls):
        """
        Returns all records for a table in the database.

        :version: 1.0.0
        :date: 2024-06-04
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        ###
        # Method is here and not in transaction as I don't see a reason to get multiple tables at once.
        ###

        stmt = select(cls)

        with SessionFactory.get_session() as session:
            ###
            # row contains a tuple where the first element is the model class, the second part of the tuple is nothing.
            # the list comprehension makes sure that all records are read and that the session can be closed.
            return [row[0] for row in session.execute(stmt)]
            ###

    @classmethod
    def query(cls, where_clause):
        """
        Returns the records from a select with where clause.

        :version: 1.0.0
        :date: 2024-06-05
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        stmt = select(cls).where(where_clause)

        with SessionFactory.get_session() as session:
            return [row[0] for row in session.execute(stmt)]
