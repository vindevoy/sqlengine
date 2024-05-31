from typing import Any

from sqlengine.common.session_factory import SessionFactory


class Transaction:
    """
    This class is created by the factory class.  It has only one instance variable, the session.
    This equals to a transaction in the RDBMS world, hence the name.

    The class holds the majority of methods to talk to the database.
    Some are also available through the base model class,
    but those only provide methods to work with one single instance.
    The transaction can, in generally, work with multiple instances at the same time.

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    def __init__(self):
        """
        Constructor method.  Only need to set the session here.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        self.__session = SessionFactory.get_session()

    def create(self, *instances) -> None:
        """
        Create one or more records in the database.
        As each of the instances are model objects, they know where to save themselves.

        :return: None

        :version: 1.0.0  You can only read records from one table in one call.
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """
        with self.__session as session:
            session.add_all(instances)
            session.commit()

    def read(self, cls,  rec_ids: list[int]) -> list:
        """
        Read one or more records in the database.  You can only read records from one table in one call.

        :return: list:
            The records read from the database.
            The type may vary, according to the cls parameter, which is used to read the records.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        ###
        # records will contain all the retrieved objects
        records = []
        ###

        with self.__session as session:
            for rec_id in rec_ids:
                record = session.get(cls, rec_id)
                records.append(record)

            return records

    def update(self, *instances) -> None:
        """
        Update one or more records in the database.

        :return: list:
            The records read from the database.
            The type may vary, according to the cls parameter, which is used to read the records.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """
        with self.__session as session:
            for instance in instances:
                current = session.get(instance.__class__, instance.id)
                column_names = instance.__class__.__table__.columns.keys()

                for column in column_names:
                    if column != "id":
                        setattr(current, column, getattr(instance, column))

            session.commit()

    def delete(self, *instances):
        """
        Delete one or more records in the database.

        :return: None

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """
        with self.__session as session:
            for instance in instances:
                session.delete(instance)

            session.commit()

    def __enter__(self) -> Any:
        """
        Entry point for the context manager.

        :return: the same class type as entered the context manager.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Exit point for the context manager.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        if exc_type is not None:
            # An exception occurred. Rollback the transaction.
            self.__session.rollback()

        # Always close the session at the end.
        self.__session.close()
