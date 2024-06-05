from sqlengine.common.output_factory import OutputFactory
from sqlengine.common.transaction_factory import TransactionFactory
from sqlengine.db import drop_db, create_db
from sqlengine.models.registration import Registration
from sqlengine.models.student import Student


def setup_test():
    drop_db.execute()
    create_db.execute()
    create_db.populate()


def test_read():
    setup_test()

    with TransactionFactory.get_transaction() as tx:
        s1 = tx.read(Student, [1])[0]

        OutputFactory.pretty_print([s1])

        assert len(s1.registrations) == 1

        OutputFactory.pretty_print(s1.registrations)

        s1.registrations = tx.read(Registration, [r.id for r in s1.registrations])

        assert s1.registrations[0].course.name == "Python Developer, second year"
        assert s1.registrations[0].student.login == "vindevoy"
        assert s1.registrations[0].school_year.description == "2023-24"
