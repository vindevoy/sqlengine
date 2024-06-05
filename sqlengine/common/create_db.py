from pathlib import Path

import pandas as pd

from sqlengine.common.drop_db import execute as drop_db_execute
from sqlengine.common.engine_factory import EngineFactory
from sqlengine.samples.course import Course
from sqlengine.samples.grade import Grade
from sqlengine.samples.registration import Registration
from sqlengine.samples.school_year import SchoolYear
from sqlengine.samples.student import Student
from sqlengine.samples.subject import Subject


def execute() -> None:
    """
    Creates the tables in the database.

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """
    engine = EngineFactory.get_engine()

    Student.metadata.create_all(engine)
    Course.metadata.create_all(engine)
    SchoolYear.metadata.create_all(engine)

    Subject.metadata.create_all(engine)  # requires Course
    Registration.metadata.create_all(engine)  # requires Course, Student and SchoolYear

    Grade.metadata.create_all(engine)  # requires Registration, Subject


def populate():
    """
    Populates the tables in the database based on the csv files.

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __populate_table("students", Student)
    __populate_table("courses", Course)
    __populate_table("school_years", SchoolYear)
    __populate_table("subjects", Subject)  # requires courses
    __populate_table("registrations", Registration)  # requires courses, students, school_years
    __populate_table("grades", Grade)  # requires registration, subjects


def __populate_table(entity: str, entity_cls):
    """
    Populates a single table using pandas for reading the csv and the model classes for writing.

    :version: 1.0.2
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    current_path = Path(__file__).parent
    csv_file = current_path.parent.joinpath("db", f"{entity}.csv")

    df = pd.read_csv(current_path.joinpath(csv_file), sep=";")

    for _, row in df.iterrows():
        ###
        # You must convert the row to a dict first, otherwise you end up with these errors:
        # sqlalchemy.exc.ProgrammingError: (psycopg2.ProgrammingError) can't adapt type 'numpy.int64'
        entity_cls(**row.to_dict()).create()
        ###

    ###
    # The code below does not maintain the column definition, fixed in 1.0.1
    # data.to_sql(table_name, engine, if_exists="replace", index=False)
    ###

    ###
    # Version history
    #
    # version: 1.0.2
    # date: 2024-06-05
    # author: Yves Vindevogel <yves@vindevogel.net>
    #
    # Converted the row to a dict first to avoid problems with numpy.int64 errors.
    #
    # version: 1.0.1
    # date: 2024-06-05
    # author: Yves Vindevogel <yves@vindevogel.net>
    #
    # No longer using the to_sql to write the records because it messes up the original column definition
    #
    # version: 1.0.0
    # date: 2024-06-05
    # author: Yves Vindevogel <yves@vindevogel.net>
    #
    # Original code
    ###


if __name__ == "__main__":
    drop_db_execute()
    execute()
    populate()

# FIXME: Add an update to the sequences for the populate
