from sqlengine.common.transaction_factory import TransactionFactory
from sqlengine.db import drop_db, create_db
from sqlengine.models.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_create():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")

    t = TransactionFactory.get_transaction()
    t.create(s1, s2)

    assert Student.record_count() == 2

    v = Student.read(rec_id=1)
    assert v.login == "vindevoy"

