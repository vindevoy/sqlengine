from sqlengine.common import drop_db, create_db
from sqlengine.common.output_factory import OutputFactory
from sqlengine.common.transaction_factory import TransactionFactory
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


def test_delete():
    setup_test()

    s = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s.create()

    assert Student.record_count() == 1

    v = Student.read(rec_id=1)
    v.delete()

    assert Student.record_count() == 0


def test_query():
    setup_test()

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")
    s3 = Student(first_name="Next", last_name="Vindevogel", login="vindevox")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2, s3)

    result = Student.query(Student.login == "vindevoy")

    assert len(result) == 1

    OutputFactory.pretty_print(result)

    result = Student.query(Student.last_name == "Vindevogel")

    assert len(result) == 3

    OutputFactory.pretty_print(result)


def test_deep_read():
    drop_db.execute()
    create_db.execute()
    create_db.populate()

    assert Student.record_count() == 3

    s1 = Student.read(rec_id=1, deep=True)

    assert len(s1.registrations) == 1

    reg = s1.registrations[0]

    assert reg.student_id == 1
    assert reg.student.login == "vindevoy"
