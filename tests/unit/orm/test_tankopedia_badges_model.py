import unittest
from wotapi.orm.data_model import TankopediaBadgesModel


class TestTankopediaBadgesORM(unittest.TestCase):

    def test_schema(self):
        p = TankopediaBadgesModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = TankopediaBadgesModel()
        self.assertEqual(p.__tablename__, 'tankopedia_badges')

    def test_columns(self):
        columns = [column.key for column in TankopediaBadgesModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'account_id', 'badge_id', 'name', 'medium_icon', 'small_icon', 'big_icon',
                         'description']

        self.assertListEqual(columns, expected_cols)
