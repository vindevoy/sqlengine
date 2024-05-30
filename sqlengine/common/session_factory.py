from sqlalchemy.orm import Session

from sqlengine.common.engine_factory import EngineFactory


class SessionFactory:
    __engine = None

    @classmethod
    def get_session(cls):
        if cls.__engine is None:
            cls.__engine = EngineFactory.get_engine()

        return Session(cls.__engine, expire_on_commit=False)
