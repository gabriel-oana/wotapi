import unittest
from wotapi.orm.data_model import TankopediaAchievementsModel


class TestTankopediaAchievementsORM(unittest.TestCase):

    def test_schema(self):
        p = TankopediaAchievementsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = TankopediaAchievementsModel()
        self.assertEqual(p.__tablename__, 'tankopedia_achievements')

    def test_columns(self):
        columns = [column.key for column in TankopediaAchievementsModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'name', 'outdated', 'section', 'section_order', 'image_big', 'options',
                         'hero_info', 'name_i18n', 'order', 'type', 'image', 'condition', 'description']

        self.assertListEqual(columns, expected_cols)
