from sqlalchemy import MetaData

from sqlengine.common.engine_factory import EngineFactory


def execute() -> None:
    """
    Drops the tables in the database.  It does not drop the complete database itself !

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    engine = EngineFactory.get_engine()
    meta = MetaData()

    meta.reflect(bind=engine)
    meta.drop_all(bind=engine)


if __name__ == '__main__':
    execute()
