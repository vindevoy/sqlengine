from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlengine.models.student import Student


def execute():
    engine = create_engine(f"postgresql://school:school@localhost/school", echo=True)

    Student.metadata.create_all(engine)


if __name__ == '__main__':
    execute()
