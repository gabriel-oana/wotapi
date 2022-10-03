import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.player_personal_data import PlayerPersonalData
from wotapi.orm.data_model import PlayerPersonalDataDetailsModel, PlayerPersonalDataStatisticsModel


class TestPlayerPersonalData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/info/',
            json=self.mock_response_player_personal(account_id=self.test_account_id),
            status=200
        )

        p = PlayerPersonalData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd()
        )

        expected_data = [{'details': [
            {'account_id': 'mock_account_id', 'last_battle_time': 1648900023, 'created_at': 1361579208,
             'updated_at': 1658457031, 'gold': 5243, 'free_xp': 14339, 'ban_time': None, 'is_bound_to_phone': True,
             'is_premium': False, 'credits': 7761405, 'premium_expires_at': 1557394809, 'bonds': 2049,
             'battle_life_time': 6239005, 'global_rating': 6187, 'clan_id': 500136157}], 'statistics': [
            {'statistic_type': 'clan', 'spotted': 0, 'battles_on_stunning_vehicles': 0, 'avg_damage_blocked': 0.0,
             'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0, 'piercings': 0,
             'max_damage_tank_id': None, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0,
             'hits_percents': 0, 'draws': 0, 'max_xp_tank_id': None, 'battles': 0, 'damage_received': 0,
             'avg_damage_assisted': 0.0, 'max_frags_tank_id': None, 'avg_damage_assisted_track': 0.0, 'frags': 0,
             'stun_number': 0, 'avg_damage_assisted_radio': 0.0, 'capture_points': 0, 'stun_assisted_damage': 0,
             'max_damage': None, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0,
             'no_damage_direct_hits_received': 0, 'max_frags': None, 'shots': 0, 'explosion_hits_received': 0,
             'tanking_factor': 0.0}, {'statistic_type': 'all', 'spotted': 18600, 'battles_on_stunning_vehicles': 254,
                                      'avg_damage_blocked': 406.24, 'direct_hits_received': 94110,
                                      'explosion_hits': 4357, 'piercings_received': 65748, 'piercings': 80139,
                                      'max_damage_tank_id': 12049, 'xp': 12150715, 'survived_battles': 5699,
                                      'dropped_capture_points': 15075, 'hits_percents': 66, 'draws': 199,
                                      'max_xp_tank_id': 54017, 'battles': 21896, 'damage_received': 20668629,
                                      'avg_damage_assisted': 340.53, 'max_frags_tank_id': 8993,
                                      'avg_damage_assisted_track': 83.72, 'frags': 19578, 'stun_number': 1449,
                                      'avg_damage_assisted_radio': 256.81, 'capture_points': 19319,
                                      'stun_assisted_damage': 164348, 'max_damage': 6776, 'hits': 130296,
                                      'battle_avg_xp': 555, 'wins': 11079, 'losses': 10618, 'damage_dealt': 24841152,
                                      'no_damage_direct_hits_received': 27153, 'max_frags': 9, 'shots': 196463,
                                      'explosion_hits_received': 5884, 'tanking_factor': 0.39},
            {'statistic_type': 'regular_team', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
             'avg_damage_blocked': 0.0, 'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0,
             'piercings': 0, 'max_damage_tank_id': None, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0,
             'hits_percents': 0, 'draws': 0, 'max_xp_tank_id': None, 'battles': 0, 'damage_received': 0,
             'avg_damage_assisted': 0.0, 'max_frags_tank_id': None, 'avg_damage_assisted_track': 0.0, 'frags': 0,
             'stun_number': 0, 'avg_damage_assisted_radio': 0.0, 'capture_points': 0, 'stun_assisted_damage': 0,
             'max_damage': 0, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0,
             'no_damage_direct_hits_received': 0, 'max_frags': 0, 'shots': 0, 'explosion_hits_received': 0,
             'tanking_factor': 0.0},
            {'statistic_type': 'company', 'spotted': 0, 'battles_on_stunning_vehicles': 0, 'avg_damage_blocked': 0.0,
             'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0, 'piercings': 0,
             'max_damage_tank_id': None, 'xp': 228, 'survived_battles': 0, 'dropped_capture_points': 0,
             'hits_percents': 50, 'draws': 0, 'max_xp_tank_id': None, 'battles': 1, 'damage_received': 460,
             'avg_damage_assisted': 0.0, 'max_frags_tank_id': None, 'avg_damage_assisted_track': 0.0, 'frags': 1,
             'stun_number': 0, 'avg_damage_assisted_radio': 0.0, 'capture_points': 0, 'stun_assisted_damage': 0,
             'max_damage': None, 'hits': 5, 'battle_avg_xp': 228, 'wins': 0, 'losses': 1, 'damage_dealt': 713,
             'no_damage_direct_hits_received': 0, 'max_frags': None, 'shots': 10, 'explosion_hits_received': 0,
             'tanking_factor': 0.0},
            {'statistic_type': 'stronghold_skirmish', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
             'avg_damage_blocked': None, 'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0,
             'piercings': 0, 'max_damage_tank_id': None, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0,
             'hits_percents': 0, 'draws': 0, 'max_xp_tank_id': None, 'battles': 0, 'damage_received': 0,
             'avg_damage_assisted': None, 'max_frags_tank_id': None, 'avg_damage_assisted_track': None, 'frags': 0,
             'stun_number': 0, 'avg_damage_assisted_radio': None, 'capture_points': 0, 'stun_assisted_damage': 0,
             'max_damage': 0, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0,
             'no_damage_direct_hits_received': 0, 'max_frags': 0, 'shots': 0, 'explosion_hits_received': 0,
             'tanking_factor': 0.0},
            {'statistic_type': 'stronghold_defense', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
             'avg_damage_blocked': None, 'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0,
             'piercings': 0, 'max_damage_tank_id': None, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0,
             'hits_percents': 0, 'draws': 0, 'max_xp_tank_id': None, 'battles': 0, 'damage_received': 0,
             'avg_damage_assisted': None, 'max_frags_tank_id': None, 'avg_damage_assisted_track': None, 'frags': 0,
             'stun_number': 0, 'avg_damage_assisted_radio': None, 'capture_points': 0, 'stun_assisted_damage': 0,
             'max_damage': 0, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0,
             'no_damage_direct_hits_received': 0, 'max_frags': 0, 'shots': 0, 'explosion_hits_received': 0,
             'tanking_factor': 0.0}, {'statistic_type': 'historical', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
                                      'avg_damage_blocked': 60.0, 'direct_hits_received': 9, 'explosion_hits': 3,
                                      'piercings_received': 8, 'piercings': 29, 'max_damage_tank_id': 7201, 'xp': 2056,
                                      'survived_battles': 2, 'dropped_capture_points': 0, 'hits_percents': 87,
                                      'draws': 0, 'max_xp_tank_id': 1057, 'battles': 4, 'damage_received': 1189,
                                      'avg_damage_assisted': 382.25, 'max_frags_tank_id': 1057,
                                      'avg_damage_assisted_track': 244.0, 'frags': 4, 'stun_number': 0,
                                      'avg_damage_assisted_radio': 138.25, 'capture_points': 0,
                                      'stun_assisted_damage': 0, 'max_damage': 1011, 'hits': 34, 'battle_avg_xp': 514,
                                      'wins': 2, 'losses': 2, 'damage_dealt': 3643, 'no_damage_direct_hits_received': 1,
                                      'max_frags': 2, 'shots': 39, 'explosion_hits_received': 0,
                                      'tanking_factor': 0.18},
            {'statistic_type': 'team', 'spotted': 59, 'battles_on_stunning_vehicles': 0, 'avg_damage_blocked': 314.26,
             'direct_hits_received': 247, 'explosion_hits': 0, 'piercings_received': 204, 'piercings': 177,
             'max_damage_tank_id': 3137, 'xp': 20870, 'survived_battles': 17, 'dropped_capture_points': 7,
             'hits_percents': 78, 'draws': 0, 'max_xp_tank_id': 5921, 'battles': 52, 'damage_received': 54056,
             'avg_damage_assisted': 193.92, 'max_frags_tank_id': 7425, 'avg_damage_assisted_track': 63.98, 'frags': 26,
             'stun_number': 0, 'avg_damage_assisted_radio': 129.94, 'capture_points': 26, 'stun_assisted_damage': 0,
             'max_damage': 3284, 'hits': 229, 'battle_avg_xp': 401, 'wins': 19, 'losses': 33, 'damage_dealt': 50293,
             'no_damage_direct_hits_received': 43, 'max_frags': 3, 'shots': 295, 'explosion_hits_received': 0,
             'tanking_factor': 0.24}]}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/info/',
            json=self.mock_response_player_personal(account_id=self.test_account_id),
            status=200
        )

        p = PlayerPersonalData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path
        )

        data_exists = self.db_loader.check_if_data_exists(model=PlayerPersonalDataDetailsModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_2(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/info/',
            json=self.mock_response_player_personal(account_id=self.test_account_id),
            status=200
        )

        p = PlayerPersonalData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path
        )

        data_exists = self.db_loader.check_if_data_exists(model=PlayerPersonalDataStatisticsModel)
        self.assertEqual(data_exists, True)
