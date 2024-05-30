from sqlalchemy import MetaData

from sqlengine.common.engine_factory import EngineFactory


def execute():
    engine = EngineFactory.get_engine()
    meta = MetaData()

    meta.reflect(bind=engine)
    meta.drop_all(bind=engine)


if __name__ == '__main__':
    execute()
