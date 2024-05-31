from pathlib import Path

import yaml
from sqlalchemy import create_engine, Engine


class EngineFactory:
    """
    The engine factory has only one purpose: to create an engine instance using the get_engine() method.
    In that method the db_settings.yaml config file is read to retrieve the username, password, and database.
    The class is implemented as a factory, meaning it uses only class methods.

    :version: 1.0.0
    :date: 2024-05-31
    :author: Yves Vindevogel <yves@vindevogel.net>
    """

    __settings = None

    __user_name: str = ""
    __password: str = ""
    __database: str = ""
    __echo: bool = False

    @classmethod
    def get_engine(cls) -> Engine:
        """
        This class method returns the SQLAlchemy engine instance, incorporating the username and password,
        along the other database connection parameters.

        :return: sqlalchemy.Engine
            The SQLAlchemy engine instance.

        :version: 1.0.0
        :date: 2024-05-31
        :author: Yves Vindevogel <yves@vindevogel.net>
        """

        if cls.__settings is None:
            current_path = Path(__file__).parent

            with open(current_path.parent.joinpath("config", "db_settings.yaml"), "r") as db_file:
                # All properties are private as only the get_engine method should be accessible.
                cls.__settings = yaml.safe_load(db_file)

                cls.__user_name = cls.__settings["user"]
                cls.__password = cls.__settings["password"]
                cls.__database = cls.__settings["database"]
                cls.__echo = bool(cls.__settings["echo"])

        return create_engine(f"postgresql://{cls.__user_name}:{cls.__password}@localhost/{cls.__database}",
                             echo=cls.__echo)
