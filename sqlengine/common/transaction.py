from sqlengine.common.session_factory import SessionFactory


class Transaction:
    def __init__(self):
        self.__session = SessionFactory.get_session()

    def create(self, *instances):
        with self.__session as session:
            session.add_all(instances)
            session.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # An exception occurred. Rollback the transaction.
            self.__session.rollback()
        # Always close the session at the end.
        self.__session.close()
