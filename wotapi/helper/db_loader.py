import os
import logging
from sqlalchemy.orm import sessionmaker

from wotapi.helper.create_engine import create_db_engine


class DBLoader:

    def __init__(self, path: str = None, db_engine=None):
        if db_engine:
            self._db_engine = db_engine
        else:
            self._db_engine = create_db_engine(path=path)

    def insert(self, model: object, data: list):
        """
        Generic method to insert a data model into sqlite.
        """

        try:
            s = sessionmaker(bind=self._db_engine)
            session = s()
            session.bulk_insert_mappings(model, data)
            session.commit()
            session.close()
            logging.info('Player vehicles data Loaded into database')

        except Exception as e:
            # TODO: Create a less generic exception
            logging.error('Player vehicles data loading data failed')
            raise RuntimeError(str(e))

    def check_if_data_exists(self, model: object):
        """
        Checks if any data is existing in the table.
        """
        s = sessionmaker(bind=self._db_engine)
        session = s()
        table_values = session.query(model).count()

        if table_values > 0:
            return True
        else:
            return False
