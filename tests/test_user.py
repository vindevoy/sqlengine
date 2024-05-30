from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlengine.models.student import Student


def test_create():
    engine = create_engine(f"postgresql://school:school@localhost/school", echo=True)

    with Session(engine) as session:
        s = Student(first_name="Yves", last_name="Vindevogel", login="vindevoy")

        session.add(s)
        session.commit()
