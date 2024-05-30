from sqlalchemy.orm import Session

from sqlengine.common.engine_factory import EngineFactory
from sqlengine.db import drop_db, create_db
from sqlengine.models.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_create():
    setup_test()

    engine = EngineFactory.get_engine()

    with Session(engine) as session:
        s = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")

        session.add(s)
        session.commit()
