from sqlalchemy import create_engine, MetaData


def execute():
    engine = create_engine(f"postgresql://school:school@localhost/school", echo=True)
    meta = MetaData()

    meta.reflect(bind=engine)
    meta.drop_all(bind=engine)


if __name__ == '__main__':
    execute()
