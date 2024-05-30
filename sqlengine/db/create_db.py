from sqlengine.common.engine_factory import EngineFactory
from sqlengine.models.student import Student


def execute():
    engine = EngineFactory.get_engine()

    Student.metadata.create_all(engine)


if __name__ == '__main__':
    execute()
