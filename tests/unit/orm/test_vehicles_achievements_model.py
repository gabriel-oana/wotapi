import unittest
from wotapi.orm.data_model import VehiclesAchievementsModel


class TestVehiclesAchievementsORM(unittest.TestCase):

    def test_schema(self):
        p = VehiclesAchievementsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = VehiclesAchievementsModel()
        self.assertEqual(p.__tablename__, 'vehicle_achievements')

    def test_columns(self):
        columns = [column.key for column in VehiclesAchievementsModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'account_id', 'tank_id', 'achievement_type', 'achievement', 'quantity']

        self.assertListEqual(columns, expected_cols)
