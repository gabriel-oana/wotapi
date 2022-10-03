import unittest
from wotapi.orm.data_model import TankopediaVehiclesModel


class TestTankopediaVehiclesORM(unittest.TestCase):

    def test_schema(self):
        p = TankopediaVehiclesModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = TankopediaVehiclesModel()
        self.assertEqual(p.__tablename__, 'tankopedia_vehicles')

    def test_columns(self):
        columns = [column.key for column in TankopediaVehiclesModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'tank_id', 'is_wheeled', 'is_premium', 'tag', 'small_icon', 'contour_icon',
                         'big_icon', 'type', 'description', 'short_name', 'name', 'nation', 'tier', 'price_gold',
                         'price_credit', 'is_gift']

        self.assertListEqual(columns, expected_cols)
