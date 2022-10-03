import unittest
from wotapi.orm.data_model import VehiclesStatisticsModel


class TestVehiclesStatisticsORM(unittest.TestCase):

    def test_schema(self):
        p = VehiclesStatisticsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_table_name(self):
        p = VehiclesStatisticsModel()
        self.assertEqual(p.__tablename__, 'vehicle_statistics')

    def test_columns(self):
        columns = [column.key for column in VehiclesStatisticsModel.__table__.columns]
        print(columns)
        expected_cols = ['id', 'loaded_at', 'account_id', 'battle_type', 'spotted', 'battles_on_stunning_vehicles',
                         'max_xp', 'xp', 'survived_battles', 'dropped_capture_points', 'hits_percents', 'draws',
                         'battles', 'damage_received', 'frags', 'stun_number', 'capture_points', 'stun_assisted_damage',
                         'max_damage', 'hits', 'battle_avg_xp', 'wins', 'losses', 'damage_dealt', 'max_frags', 'shots',
                         'direct_hits_received', 'explosion_hits', 'piercings_received', 'piercings',
                         'no_damage_direct_hits_received', 'explosion_hits_received', 'tanking_factor',
                         'avg_damage_blocked', 'mark_of_mastery', 'in_garage', 'tank_id']

        self.assertListEqual(columns, expected_cols)
