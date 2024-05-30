from sqlengine.common.session_factory import SessionFactory


class Transaction:
    def __init__(self):
        self.__session = SessionFactory.get_session()

    def create(self, *args):
        with self.__session as session:
            session.add_all(args)
            session.commit()
