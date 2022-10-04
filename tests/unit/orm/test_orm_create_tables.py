import unittest
from sqlalchemy import create_engine
from sqlalchemy import inspect

from wotapi.orm.data_model import DataModel


class TestDataModel(unittest.TestCase):

    def test_all_tables_get_created(self):
        engine = create_engine('sqlite:///:memory:')
        DataModel.create_tables(engine=engine)
        inspector = inspect(engine)
        schemas = inspector.get_schema_names()

        table_names = []
        for schema in schemas:
            for table_name in inspector.get_table_names(schema=schema):
                table_names.append(table_name)

        expected_tables = ['player_achievements', 'player_personal_details', 'player_personal_statistics',
                           'player_vehicles', 'tankopedia_achievements', 'tankopedia_badges', 'tankopedia_information',
                           'tankopedia_maps', 'tankopedia_vehicles', 'vehicle_achievements', 'vehicle_frags',
                           'vehicle_statistics']

        self.assertListEqual(table_names, expected_tables)
