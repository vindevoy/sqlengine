from sqlengine.common import drop_db, create_db
from sqlengine.common.output_factory import OutputFactory
from sqlengine.common.transaction_factory import TransactionFactory
from sqlengine.samples.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_create():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2)

    assert Student.record_count() == 2

    v = Student.read(rec_id=1)
    assert v.login == "vindevoy"


def test_create_no_context():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")

    t = TransactionFactory.get_transaction()
    t.create(s1, s2)

    assert Student.record_count() == 2

    v = Student.read(rec_id=1)
    assert v.login == "vindevoy"


def test_delete():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")
    s3 = Student(first_name="Next", last_name="Vindevogel", login="vindevox")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2, s3)

    assert Student.record_count() == 3

    v1 = Student.read(rec_id=1)
    v2 = Student.read(rec_id=2)
    v3 = Student.read(rec_id=3)

    with TransactionFactory.get_transaction() as t:
        t.delete(v1)

    assert Student.record_count() == 2

    with TransactionFactory.get_transaction() as t:
        t.delete(v2, v3)

    assert Student.record_count() == 0


def test_read():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")
    s3 = Student(first_name="Next", last_name="Vindevogel", login="vindevox")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2, s3)

    with TransactionFactory.get_transaction() as t:
        lst = t.read(Student, [1, 3])

        v1 = lst[0]
        v3 = lst[1]

        assert v1.login == "vindevoy"
        assert v3.login == "vindevox"


def test_all():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")
    s3 = Student(first_name="Next", last_name="Vindevogel", login="vindevox")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2, s3)

    result = Student.all()

    assert len(result) == 3
    assert type(result) is list
    assert type(result[0]) is Student

    assert result[0].login == "vindevoy"
    assert result[1].login == "vindevon"
    assert result[2].login == "vindevox"

    OutputFactory.pretty_print(result)


def test_delete_ids():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")
    s3 = Student(first_name="Next", last_name="Vindevogel", login="vindevox")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2, s3)

    assert Student.record_count() == 3

    with TransactionFactory.get_transaction() as t:
        t.delete_ids(Student, [1, 2])

    assert Student.record_count() == 1
