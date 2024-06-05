from sqlengine.common import drop_db, create_db
from sqlengine.common.output_factory import OutputFactory
from sqlengine.common.transaction_factory import TransactionFactory
from sqlengine.models.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_output():
    setup_test()

    assert Student.record_count() == 0

    s1 = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")
    s2 = Student(first_name="Niels", last_name="Vindevogel", login="vindevon")
    s3 = Student(first_name="Next", last_name="Vindevogel", login="vindevox")

    with TransactionFactory.get_transaction() as t:
        t.create(s1, s2, s3)

    result = Student.all()

    OutputFactory.pretty_print(result)
