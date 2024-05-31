from sqlalchemy.orm import Session

from sqlengine.common.engine_factory import EngineFactory


class SessionFactory:
    """
    The session factory is used to create a new database session based on SQLAlchemy.

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __engine = None

    @classmethod
    def get_session(cls) -> Session:
        """
        This class method returns the SQLAlchemy session instance.
        Following defaults are set:

            - expire_on_commit = False

        :return: sqlalchemy.orm.Session
            The SQLAlchemy session instance.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        if cls.__engine is None:
            cls.__engine = EngineFactory.get_engine()

        return Session(cls.__engine, expire_on_commit=False)
