from sqlengine.db import drop_db, create_db
from sqlengine.models.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_create():
    setup_test()

    s = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s.create()

    v = Student.read(rec_id=1)

    assert v.id == 1
    assert v.first_name == "Yves"
    assert v.last_name == "Vindevogel"
    assert v.login == "vindevoy"


def test_update():
    setup_test()

    s = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s.create()

    v = Student.read(rec_id=1)
    v.login = "sidviny"
    v.update()

    u = Student.read(rec_id=1)

    assert u.id == 1
    assert u.first_name == "Yves"
    assert u.last_name == "Vindevogel"
    assert u.login == "sidviny"
