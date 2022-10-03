from sqlalchemy import create_engine


def create_db_engine(path: str):
    """
    Creates a sqlite database to be populated by the ORM
    """
    engine = create_engine(f'sqlite:///{path}/world_of_tanks.db')

    return engine
