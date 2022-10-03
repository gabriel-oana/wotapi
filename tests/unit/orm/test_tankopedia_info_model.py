import unittest
from wotapi.orm.data_model import TankopediaInfoModel


class TestTankopediaVehiclesORM(unittest.TestCase):

    def test_schema(self):
        p = TankopediaInfoModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = TankopediaInfoModel()
        self.assertEqual(p.__tablename__, 'tankopedia_information')

    def test_columns(self):
        columns = [column.key for column in TankopediaInfoModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'metric', 'group', 'alias', 'value']

        self.assertListEqual(columns, expected_cols)
