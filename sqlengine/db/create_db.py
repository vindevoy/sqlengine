from sqlengine.common.engine_factory import EngineFactory
from sqlengine.models.student import Student


def execute() -> None:
    """
    Creates the tables in the database.

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """
    engine = EngineFactory.get_engine()

    Student.metadata.create_all(engine)


if __name__ == '__main__':
    execute()
