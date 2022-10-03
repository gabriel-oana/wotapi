import unittest
from wotapi.orm.data_model import PlayerPersonalDataDetailsModel, PlayerPersonalDataStatisticsModel


class TestPlayerPersonalDataORM(unittest.TestCase):

    def test_player_personal_data_schema(self):
        p = PlayerPersonalDataDetailsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_player_personal_data_table_name(self):
        p = PlayerPersonalDataDetailsModel()
        self.assertEqual(p.__tablename__, 'player_personal_details')

    def test_player_personal_data_columns(self):
        columns = [column.key for column in PlayerPersonalDataDetailsModel.__table__.columns]
        expected_cols = ['id', 'loaded_at', 'last_battle_time', 'account_id', 'created_at', 'updated_at', 'gold',
                         'free_xp', 'ban_time', 'is_bound_to_phone', 'is_premium', 'credits', 'premium_expires_at',
                         'bonds', 'battle_life_time', 'global_rating', 'clan_id']

        self.assertListEqual(columns, expected_cols)

    def test_player_personal_data_statistics_schema(self):
        p = PlayerPersonalDataStatisticsModel()
        schema = p.__table_args__['schema']
        self.assertEqual(schema, 'main')

    def test_player_personal_data_statistics_table_name(self):
        p = PlayerPersonalDataStatisticsModel()
        self.assertEqual(p.__tablename__, 'player_personal_statistics')

    def test_player_personal_data_statistics_columns(self):
        columns = [column.key for column in PlayerPersonalDataStatisticsModel.__table__.columns]
        expected_cols = ['id', 'loaded_at', 'statistic_type', 'spotted', 'battles_on_stunning_vehicles',
                         'avg_damage_blocked', 'direct_hits_received', 'explosion_hits', 'piercings_received',
                         'piercings', 'max_damage_tank_id', 'max_xp_tank_id', 'max_frags', 'xp', 'survived_battles',
                         'dropped_capture_points', 'hits_received', 'hits_percents', 'max_damage', 'draws', 'battles',
                         'damage_received', 'avg_damage_assisted', 'avg_damage_assisted_track', 'frags', 'stun_number',
                         'avg_damage_assisted_radio', 'capture_points', 'stun_assisted_damage', 'hits', 'battle_avg_xp',
                         'wins', 'losses', 'damage_dealt', 'no_damage_direct_hits_received', 'shots',
                         'explosion_hits_received', 'tanking_factor', 'max_frags_tank_id']

        self.assertListEqual(columns, expected_cols)
