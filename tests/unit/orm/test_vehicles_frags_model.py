import unittest
from wotapi.orm.data_model import VehiclesFragsModel


class TestVehiclesFragsORM(unittest.TestCase):

    def test_schema(self):
        p = VehiclesFragsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = VehiclesFragsModel()
        self.assertEqual(p.__tablename__, 'vehicle_frags')

    def test_columns(self):
        columns = [column.key for column in VehiclesFragsModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'account_id', 'tank_id', 'opponent_tank_id', 'frags']

        self.assertListEqual(columns, expected_cols)
