from sqlengine.common.session_factory import SessionFactory
from sqlengine.db import drop_db, create_db
from sqlengine.models.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_create():
    setup_test()

    s = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s.create()
