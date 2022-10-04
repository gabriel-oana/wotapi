import unittest
from wotapi.orm.data_model import PlayerAchievementsModel


class TestPlayerAchievementsDataORM(unittest.TestCase):

    def test_player_achievements_vehicles_schema(self):
        p = PlayerAchievementsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_player_achievements_vehicles_table_name(self):
        p = PlayerAchievementsModel()
        self.assertEqual(p.__tablename__, 'player_achievements')

    def test_player_achievements_data_columns(self):
        columns = [column.key for column in PlayerAchievementsModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'medal_type', 'medal_name', 'medal_quantity']

        self.assertListEqual(columns, expected_cols)

