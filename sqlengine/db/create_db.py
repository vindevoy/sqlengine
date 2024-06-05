from pathlib import Path

import pandas as pd

from sqlengine.common.engine_factory import EngineFactory
from sqlengine.models.student import Student


def execute() -> None:
    """
    Creates the tables in the database.

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """
    engine = EngineFactory.get_engine()

    Student.metadata.create_all(engine)


def populate():
    """
    Populates the tables in the database based on the csv files.

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __populate_table("tbl_students", "students.csv")


def __populate_table(table_name: str, csv_file: str):
    """
    Populates a single table using pandas.

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    engine = EngineFactory.get_engine()
    current_path = Path(__file__).parent

    data = pd.read_csv(current_path.joinpath(csv_file), sep=";")
    data.to_sql(table_name, engine, if_exists="replace", index=False)


if __name__ == "__main__":
    execute()
    populate()
