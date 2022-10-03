import unittest
from wotapi.orm.data_model import TankopediaMapsModel


class TestTankopediaVehiclesORM(unittest.TestCase):

    def test_schema(self):
        p = TankopediaMapsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = TankopediaMapsModel()
        self.assertEqual(p.__tablename__, 'tankopedia_maps')

    def test_columns(self):
        columns = [column.key for column in TankopediaMapsModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'name', 'camouflage_type', 'description', 'arena_id']

        self.assertListEqual(columns, expected_cols)
