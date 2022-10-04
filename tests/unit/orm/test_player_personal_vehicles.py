import unittest
from wotapi.orm.data_model import PlayerPersonalVehiclesModel


class TestPlayerPersonalVehiclesORM(unittest.TestCase):

    def test_player_personal_vehicles_schema(self):
        p = PlayerPersonalVehiclesModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_player_personal_vehicles_table_name(self):
        p = PlayerPersonalVehiclesModel()
        self.assertEqual(p.__tablename__, 'player_vehicles')

    def test_player_personal_data_columns(self):
        columns = [column.key for column in PlayerPersonalVehiclesModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'tank_id', 'battles', 'mark_of_mastery']

        self.assertListEqual(columns, expected_cols)

