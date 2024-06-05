from pathlib import Path

import pandas as pd

from sqlengine.common.engine_factory import EngineFactory


def execute() -> None:
    """
    Outputs the tables in the database to a .csv file

    :version: 1.0.0
    :date: 2024-06-05
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    tables = ["courses", "grades", "registrations", "school_years", "students", "subjects"]

    engine = EngineFactory.get_engine()
    current_path = Path(__file__).parent

    for table in tables:
        sql_query = f"SELECT * FROM tbl_{table}"  # noqa

        df = pd.read_sql(sql_query, engine)

        # Make sure "id" is the first column
        columns = ["id"]
        columns.extend(c for c in df.columns if c != "id")

        df.to_csv(current_path.parent.joinpath("db", f"{table}.csv"), index=False, sep=";", columns=columns)

    engine.dispose()


if __name__ == "__main__":
    execute()
