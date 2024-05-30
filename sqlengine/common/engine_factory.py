from pathlib import Path

import yaml
from sqlalchemy import create_engine


class EngineFactory:
    __settings = None

    __user_name: str = ""
    __password: str = ""
    __database: str = ""
    __echo: bool = False

    @classmethod
    def __init(cls):
        print("init EngineFactory")
        current_path = Path(__file__).parent

        with open(current_path.parent.joinpath("config", "db_settings.yaml"), "r") as db_file:
            cls.__settings = yaml.safe_load(db_file)

            cls.__user_name = cls.__settings["user"]
            cls.__password = cls.__settings["password"]
            cls.__database = cls.__settings["database"]
            cls.__echo = bool(cls.__settings["echo"])

    @classmethod
    def get_engine(cls):
        if cls.__settings is None:
            cls.__init()

        return create_engine(f"postgresql://{cls.__user_name}:{cls.__password}@localhost/{cls.__database}",
                             echo=cls.__echo)
