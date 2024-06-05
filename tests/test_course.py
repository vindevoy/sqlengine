from sqlengine.common import drop_db, create_db
from sqlengine.common.transaction_factory import TransactionFactory
from sqlengine.models.course import Course
from sqlengine.models.subject import Subject


def setup_test():
    drop_db.execute()
    create_db.execute()


def test_create():
    setup_test()

    with TransactionFactory.get_transaction() as tx:
        c1 = Course(mnemonic="python_1", name="Python Developer, first year")
        tx.create(c1)

        s1 = Subject(mnemonic="py_start", name="Starting with Programming", course_id=c1.id)
        tx.create(s1)

        s2 = Subject(mnemonic="py_func_prog", name="Functional Programming in Python", course=c1)
        tx.create(s2)

        c2 = Course(mnemonic="python_2", name="Python Developer, second year")
        tx.create(c2)

    assert Course.record_count() == 2
    assert Subject.record_count() == 2


def test_multi_create():
    setup_test()

    with TransactionFactory.get_transaction() as tx:
        c1 = Course(mnemonic="python_1", name="Python Developer, first year")
        s1 = Subject(mnemonic="py_start", name="Starting with Programming", course=c1)
        s2 = Subject(mnemonic="py_func_prog", name="Functional Programming in Python", course=c1)

        tx.create(c1, s1, s2)

    assert Course.record_count() == 1
    assert Subject.record_count() == 2


def test_no_tx():
    setup_test()

    c1 = Course(mnemonic="python_1", name="Python Developer, first year")
    c1.create()

    s1 = Subject(mnemonic="py_start", name="Starting with Programming", course_id=c1.id)
    s1.create()

    s2 = Subject(mnemonic="py_func_prog", name="Functional Programming in Python", course=c1)
    s2.create()

    assert Course.record_count() == 1
    assert Subject.record_count() == 2


def test_append():
    setup_test()

    c1 = Course(mnemonic="python_1", name="Python Developer, first year")
    s1 = Subject(mnemonic="py_start", name="Starting with Programming", course_id=c1.id)
    s2 = Subject(mnemonic="py_func_prog", name="Functional Programming in Python", course=c1)

    c1.subjects.append(s1)
    c1.subjects.append(s2)

    c1.create()

    assert Course.record_count() == 1
    assert Subject.record_count() == 2


def test_read():
    setup_test()

    with TransactionFactory.get_transaction() as tx:
        c1 = Course(mnemonic="python_1", name="Python Developer, first year")
        s1 = Subject(mnemonic="py_start", name="Starting with Programming", course=c1)
        s2 = Subject(mnemonic="py_func_prog", name="Functional Programming in Python", course=c1)

        tx.create(c1, s1, s2)

    c = Course.read(1)

    assert c.mnemonic == "python_1"
    assert c.name == "Python Developer, first year"

    assert len(c.subjects) == 2

    assert c.subjects[0].mnemonic == "py_start"
    assert c.subjects[0].name == "Starting with Programming"
    assert c.subjects[0].course_id == c1.id

    assert c.subjects[1].mnemonic == "py_func_prog"
    assert c.subjects[1].name == "Functional Programming in Python"
    assert c.subjects[1].course_id == c1.id
