import responses

from tests.unit.test_wrapper import TestWrapper
from wotapi.wotapi import WotAPI
from wotapi.orm.data_model import TankopediaMapsModel


class TestWotAPI(TestWrapper):

    @responses.activate
    def test_get_account_id(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/list/',
            json=self.mock_account_id(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.get_account_id(
            nickname='mock-nickname'
        )
        self.assertEqual(response, 1)

    @responses.activate
    def test_renew_token(self):
        responses.add(
            responses.POST,
            'https://api.worldoftanks.eu/wot/auth/prolongate/',
            json=self.mock_renew_access_token(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.renew_token()
        expected_response = {'status': 'ok', 'meta': {'count': 3},
                             'data': {'access_token': '49a5800faeb33fcc49adb62dfbccc912b8694cec',
                                      'account_id': 'mock_account_id', 'expires_at': 1666035021}}
        self.assertDictEqual(response, expected_response)

    @responses.activate
    def test_player_personal(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/info/',
            json=self.mock_response_player_personal(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.player_personal(load_to_db=False)
        print(response)
        expected_response = [{'details': [
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
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_player_vehicles(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/tanks/',
            json=self.mock_response_vehicles_data(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.player_vehicles(load_to_db=False)
        print(response)
        expected_response = [{'tank_id': 8993, 'battles': 921, 'mark_of_mastery': 4, 'wins': 454},
                             {'tank_id': 54865, 'battles': 1, 'mark_of_mastery': 1, 'wins': 1}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_player_achievements(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/achievements/',
            json=self.mock_response_player_achievements(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.player_achievements(load_to_db=False)
        print(response)
        expected_response = [{'medal_type': 'achievements', 'medal_name': 'medalCarius', 'medal_quantity': 1},
                             {'medal_type': 'frags', 'medal_name': 'crucialShotMedal', 'medal_quantity': 3},
                             {'medal_type': 'max_series', 'medal_name': 'armorPiercer', 'medal_quantity': 23}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_tankopedia_vehicles(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/',
            json=self.mock_tankopedia_vehicles(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.tankopedia_vehicles(load_to_db=False, load_once=False)
        print(response)
        expected_response = [{'tank_id': 1, 'is_wheeled': False, 'is_premium': False, 'tag': 'R04_T-34',
                              'small_icon': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/vehicle/small/ussr-R04_T-34.png',
                              'contour_icon': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/vehicle/contour/ussr-R04_T-34.png',
                              'big_icon': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/vehicle/ussr-R04_T-34.png',
                              'type': 'mediumTank',
                              'description': 'The legend of the Soviet armored forces and the most widely-produced Soviet tank of World War II, with a total of 33,805 vehicles manufactured. Three variants of this model were produced at several Soviet factories from 1940 through 1944.',
                              'short_name': 'T-34', 'nation': 'ussr', 'tier': 5, 'is_gift': False, 'name': 'T-34',
                              'price_gold': 0, 'price_credit': 356700}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_tankopedia_achievements(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/achievements/',
            json=self.mock_tankopedia_achievements(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.tankopedia_achievements(load_to_db=False, load_once=False)
        print(response)
        expected_response = [{'name': 'crucialShotMedal', 'outdated': False, 'section': 'special', 'section_order': 1,
                              'image_big': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/achievement/big/crucialShotMedal.png',
                              'hero_info': None, 'name_i18n': 'Crucial Shot', 'order': 105, 'type': 'repeatable',
                              'image': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/achievement/crucialShotMedal.png',
                              'condition': ' Win the battle.\n Newly received awards are added together.\n Can be obtained in Team Battles only.',
                              'description': 'In 20 battles, destroy the last enemy vehicle.'},
                             {'name': 'Mastery Badge: "Class III"', 'outdated': False, 'section': 'class',
                              'section_order': 5,
                              'image_big': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/achievement/markOfMastery1.png',
                              'hero_info': None, 'name_i18n': 'Mastery Badge: ""', 'order': -1, 'type': 'class',
                              'image': 'http://api.worldoftanks.eu/static/2.71.0/wot/encyclopedia/achievement/markOfMastery1.png',
                              'condition': ' Statistics show the maximum rank\nof mastery.\n A newly received current rank is displayed\nin the battle results window.\n Can be obtained in Random Battles only.',
                              'description': 'Awarded for mastery in controlling an armored\nvehicle. To qualify, a player must earn more\nexperience in a battle than the average highest\nexperience of 50% players who have fought\nin this vehicle for the previous 7 days.'}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_tankopedia_information(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/info/',
            json=self.mock_tankopedia_info(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.tankopedia_information(load_to_db=False, load_once=False)
        print(response)
        expected_response = [{'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'loader', 'value': 'Loader'},
                             {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'radioman',
                              'value': 'Radio Operator'},
                             {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'driver', 'value': 'Driver'},
                             {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'gunner', 'value': 'Gunner'},
                             {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'commander',
                              'value': 'Commander'},
                             {'metric': 'languages', 'group': None, 'alias': 'ru', 'value': 'Русский'},
                             {'metric': 'languages', 'group': None, 'alias': 'fr', 'value': 'Français'},
                             {'metric': 'languages', 'group': None, 'alias': 'en', 'value': 'English'},
                             {'metric': 'languages', 'group': None, 'alias': 'zh-tw', 'value': '繁體中文'},
                             {'metric': 'languages', 'group': None, 'alias': 'de', 'value': 'Deutsch'},
                             {'metric': 'languages', 'group': None, 'alias': 'tr', 'value': 'Türkçe'},
                             {'metric': 'languages', 'group': None, 'alias': 'ko', 'value': '한국어'},
                             {'metric': 'languages', 'group': None, 'alias': 'zh-cn', 'value': '简体中文'},
                             {'metric': 'languages', 'group': None, 'alias': 'es', 'value': 'Español'},
                             {'metric': 'languages', 'group': None, 'alias': 'th', 'value': 'ไทย'},
                             {'metric': 'languages', 'group': None, 'alias': 'vi', 'value': 'Tiếng Việt'},
                             {'metric': 'languages', 'group': None, 'alias': 'cs', 'value': 'Čeština'},
                             {'metric': 'languages', 'group': None, 'alias': 'pl', 'value': 'Polski'},
                             {'metric': 'vehicle_types', 'group': None, 'alias': 'heavyTank', 'value': 'Heavy Tank'},
                             {'metric': 'vehicle_types', 'group': None, 'alias': 'AT-SPG', 'value': 'Tank Destroyer'},
                             {'metric': 'vehicle_types', 'group': None, 'alias': 'mediumTank', 'value': 'Medium Tank'},
                             {'metric': 'vehicle_types', 'group': None, 'alias': 'lightTank', 'value': 'Light Tank'},
                             {'metric': 'vehicle_types', 'group': None, 'alias': 'SPG', 'value': 'SPG'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'italy', 'value': 'Italy'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'usa', 'value': 'U.S.A.'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'czech', 'value': 'Czechoslovakia'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'poland', 'value': 'Poland'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'france', 'value': 'France'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'sweden', 'value': 'Sweden'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'ussr', 'value': 'U.S.S.R.'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'china', 'value': 'China'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'uk', 'value': 'U.K.'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'japan', 'value': 'Japan'},
                             {'metric': 'vehicle_nations', 'group': None, 'alias': 'germany', 'value': 'Germany'},
                             {'metric': 'achievement_sections', 'group': 'memorial', 'alias': 'Commemorative Tokens',
                              'value': 4},
                             {'metric': 'achievement_sections', 'group': 'group', 'alias': 'Group Awards', 'value': 3},
                             {'metric': 'achievement_sections', 'group': 'action', 'alias': 'Special', 'value': 6},
                             {'metric': 'achievement_sections', 'group': 'battle', 'alias': 'Battle Heroes',
                              'value': 0},
                             {'metric': 'achievement_sections', 'group': 'epic', 'alias': 'Epic Medals', 'value': 2},
                             {'metric': 'achievement_sections', 'group': 'class', 'alias': 'Stage Awards', 'value': 5},
                             {'metric': 'achievement_sections', 'group': 'special', 'alias': 'Honorary Ranks',
                              'value': 1}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_tankopedia_maps(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/arenas/',
            json=self.mock_tankopedia_maps(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.tankopedia_maps(load_to_db=False, load_once=False)
        print(response)
        expected_response = [{'name': 'Ruinberg', 'camouflage_type': 'summer', 'description': 'Some description',
                              'arena_id': '08_ruinberg'}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_tankopedia_badges(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/badges/',
            json=self.mock_tankopedia_badges(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.tankopedia_badges(load_to_db=False, load_once=False)
        print(response)
        expected_response = [{'account_id': 'mock_account_id', 'badge_id': 1, 'name': 'Gold, Beta Season',
                              'description': 'Reach League I in Beta Season of the Ranked Battle mode.',
                              'medium_icon': 'http://badge_1.png', 'small_icon': 'http://badge_1.png',
                              'big_icon': 'http://badge_1.png'}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_vehicle_statistics(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/tanks/stats/',
            json=self.mock_response_vehicles_statistics(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.vehicle_statistics(load_to_db=False)
        expected_response = [{'statistics_data': [
            {'account_id': 'mock_account_id', 'battle_type': 'clan', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
             'max_xp': 2230, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0, 'hits_percents': 0,
             'draws': 0, 'battles': 0, 'damage_received': 0, 'frags': 0, 'stun_number': 0, 'capture_points': 0,
             'stun_assisted_damage': 0, 'max_damage': 0, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0,
             'damage_dealt': 0, 'max_frags': 9, 'shots': 0, 'direct_hits_received': None, 'explosion_hits': None,
             'piercings_received': None, 'piercings': None, 'no_damage_direct_hits_received': None,
             'explosion_hits_received': None, 'tanking_factor': None, 'avg_damage_blocked': None, 'mark_of_mastery': 4,
             'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'all', 'spotted': 1029, 'battles_on_stunning_vehicles': 0,
             'max_xp': 2230, 'xp': 634958, 'survived_battles': 260, 'dropped_capture_points': 814, 'hits_percents': 76,
             'draws': 7, 'battles': 921, 'damage_received': 1359820, 'frags': 1024, 'stun_number': 0,
             'capture_points': 347, 'stun_assisted_damage': 0, 'max_damage': None, 'hits': 7371, 'battle_avg_xp': 689,
             'wins': 454, 'losses': 460, 'damage_dealt': 1682530, 'max_frags': 9, 'shots': 9666,
             'direct_hits_received': 4879, 'explosion_hits': 2, 'piercings_received': 3902, 'piercings': 5043,
             'no_damage_direct_hits_received': 970, 'explosion_hits_received': 285, 'tanking_factor': 0.19,
             'avg_damage_blocked': 275.15, 'mark_of_mastery': 4, 'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'regular_team', 'spotted': 0,
             'battles_on_stunning_vehicles': 0, 'max_xp': 2230, 'xp': 0, 'survived_battles': 0,
             'dropped_capture_points': 0, 'hits_percents': 0, 'draws': 0, 'battles': 0, 'damage_received': 0,
             'frags': 0, 'stun_number': 0, 'capture_points': 0, 'stun_assisted_damage': 0, 'max_damage': 0, 'hits': 0,
             'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0, 'max_frags': 9, 'shots': 0,
             'direct_hits_received': None, 'explosion_hits': None, 'piercings_received': None, 'piercings': None,
             'no_damage_direct_hits_received': None, 'explosion_hits_received': None, 'tanking_factor': None,
             'avg_damage_blocked': None, 'mark_of_mastery': 4, 'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'company', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
             'max_xp': 2230, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0, 'hits_percents': 0,
             'draws': 0, 'battles': 0, 'damage_received': 0, 'frags': 0, 'stun_number': 0, 'capture_points': 0,
             'stun_assisted_damage': 0, 'max_damage': None, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0,
             'damage_dealt': 0, 'max_frags': 9, 'shots': 0, 'direct_hits_received': None, 'explosion_hits': None,
             'piercings_received': None, 'piercings': None, 'no_damage_direct_hits_received': None,
             'explosion_hits_received': None, 'tanking_factor': None, 'avg_damage_blocked': None, 'mark_of_mastery': 4,
             'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'stronghold_skirmish', 'spotted': 0,
             'battles_on_stunning_vehicles': 0, 'max_xp': 2230, 'xp': 0, 'survived_battles': 0,
             'dropped_capture_points': 0, 'hits_percents': 0, 'draws': 0, 'battles': 0, 'damage_received': 0,
             'frags': 0, 'stun_number': 0, 'capture_points': 0, 'stun_assisted_damage': 0, 'max_damage': 0, 'hits': 0,
             'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0, 'max_frags': 9, 'shots': 0,
             'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0, 'piercings': 0,
             'no_damage_direct_hits_received': 0, 'explosion_hits_received': 0, 'tanking_factor': 0.0,
             'avg_damage_blocked': None, 'mark_of_mastery': 4, 'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'stronghold_defense', 'spotted': 0,
             'battles_on_stunning_vehicles': 0, 'max_xp': 2230, 'xp': 0, 'survived_battles': 0,
             'dropped_capture_points': 0, 'hits_percents': 0, 'draws': 0, 'battles': 0, 'damage_received': 0,
             'frags': 0, 'stun_number': 0, 'capture_points': 0, 'stun_assisted_damage': 0, 'max_damage': 0, 'hits': 0,
             'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0, 'max_frags': 9, 'shots': 0,
             'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0, 'piercings': 0,
             'no_damage_direct_hits_received': 0, 'explosion_hits_received': 0, 'tanking_factor': 0.0,
             'avg_damage_blocked': None, 'mark_of_mastery': 4, 'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'globalmap', 'spotted': 0,
             'battles_on_stunning_vehicles': 0, 'max_xp': 2230, 'xp': 0, 'survived_battles': 0,
             'dropped_capture_points': 0, 'hits_percents': 0, 'draws': 0, 'battles': 0, 'damage_received': 0,
             'frags': 0, 'stun_number': 0, 'capture_points': 0, 'stun_assisted_damage': 0, 'max_damage': None,
             'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0, 'damage_dealt': 0, 'max_frags': 9, 'shots': 0,
             'direct_hits_received': 0, 'explosion_hits': 0, 'piercings_received': 0, 'piercings': 0,
             'no_damage_direct_hits_received': 0, 'explosion_hits_received': 0, 'tanking_factor': 0.0,
             'avg_damage_blocked': 0.0, 'mark_of_mastery': 4, 'in_garage': True, 'tank_id': 8993},
            {'account_id': 'mock_account_id', 'battle_type': 'team', 'spotted': 0, 'battles_on_stunning_vehicles': 0,
             'max_xp': 2230, 'xp': 0, 'survived_battles': 0, 'dropped_capture_points': 0, 'hits_percents': 0,
             'draws': 0, 'battles': 0, 'damage_received': 0, 'frags': 0, 'stun_number': 0, 'capture_points': 0,
             'stun_assisted_damage': 0, 'max_damage': 0, 'hits': 0, 'battle_avg_xp': 0, 'wins': 0, 'losses': 0,
             'damage_dealt': 0, 'max_frags': 9, 'shots': 0, 'direct_hits_received': None, 'explosion_hits': None,
             'piercings_received': None, 'piercings': None, 'no_damage_direct_hits_received': None,
             'explosion_hits_received': None, 'tanking_factor': None, 'avg_damage_blocked': None, 'mark_of_mastery': 4,
             'in_garage': True, 'tank_id': 8993}], 'frags_data': [
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3921', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2961', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2849', 'frags': 14},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5713', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '17473', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2657', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '64065', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '15393', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2097', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7953', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4225', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5457', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7457', 'frags': 11},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13089', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '55297', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13569', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4145', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '63793', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5377', 'frags': 28},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1073', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4385', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16161', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3857', 'frags': 9},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7697', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10817', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '62785', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '817', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13841', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11025', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16673', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14353', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8225', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14673', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '50961', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '6465', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '64561', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '57121', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '15425', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3137', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3649', 'frags': 17},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7969', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '54289', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7441', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4737', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '6657', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5185', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11537', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13313', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '18449', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '12305', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '17953', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5697', 'frags': 16},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8705', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '59649', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1665', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10753', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8977', 'frags': 9},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13857', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '18177', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '19201', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13889', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1921', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8529', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '273', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '18961', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '6145', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10513', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '64049', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '22017', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '21505', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '51361', 'frags': 10},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '52097', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2305', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7249', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5969', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '12097', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '18241', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11601', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2177', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8737', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8961', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5681', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '529', 'frags': 11},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16129', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2417', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16897', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16657', 'frags': 14},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '15953', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4193', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '305', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3153', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '50193', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9489', 'frags': 10},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '19969', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10785', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16401', 'frags': 23},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4353', 'frags': 13},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14337', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11009', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1297', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '15681', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7425', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '55633', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8721', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '513', 'frags': 11},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2161', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11297', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4113', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9249', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '59169', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '59905', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '20737', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2593', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16641', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14609', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '15649', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4433', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8465', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5137', 'frags': 17},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '48641', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1905', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '63297', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10257', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10001', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8193', 'frags': 10},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3217', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2209', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1585', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '57377', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '18753', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '55313', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1121', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7233', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10017', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '6209', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14625', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '63041', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '49665', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3873', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9505', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9745', 'frags': 16},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14145', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10241', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7489', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9233', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7169', 'frags': 9},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '61713', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3377', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3681', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3889', 'frags': 12},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16417', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '57889', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '60945', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1841', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11521', 'frags': 26},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3905', 'frags': 18},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2865', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '7937', 'frags': 17},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2433', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3633', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14401', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '12369', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '12545', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '60177', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '15377', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13345', 'frags': 11},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5889', 'frags': 6},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '16913', 'frags': 9},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '58913', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '63553', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '49409', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '61761', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '12113', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '49', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11073', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4929', 'frags': 22},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '18209', 'frags': 11},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13137', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8449', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '1569', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '17217', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '5921', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '10769', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '19745', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14865', 'frags': 11},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4097', 'frags': 4},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '2721', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '61505', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '52561', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '52609', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11041', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '17665', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14161', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '12049', 'frags': 9},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9217', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '13825', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '21249', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '17153', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '9297', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11793', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8993', 'frags': 8},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '4913', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '3425', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '64817', 'frags': 1},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '19217', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '8481', 'frags': 5},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '62017', 'frags': 3},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '14881', 'frags': 7},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '55569', 'frags': 2},
            {'account_id': 'mock_account_id', 'tank_id': 8993, 'opponent_tank_id': '11841', 'frags': 4}]}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_vehicle_achievements(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/tanks/achievements/',
            json=self.mock_response_vehicles_achievements(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            load_to_db=False,
            logging_enabled=True
        )
        response = wotapi.vehicle_achievements(load_to_db=False)
        print(response)
        expected_response = [{'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                              'achievement': 'medalCarius', 'quantity': 4},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                              'achievement': 'titleSniper', 'quantity': 14},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                              'achievement': 'markOfMastery', 'quantity': 1},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                              'achievement': 'armorPiercer', 'quantity': 14},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'armorPiercer', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'aimer', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'titleSniper', 'quantity': 10},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'deathTrack', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'invincible', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'victoryMarch', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'EFC2016', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'diehard', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'WFC2014', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'tacticalBreakthrough', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                              'achievement': 'handOfDeath', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'armorPiercer', 'quantity': 14},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'aimer', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'titleSniper', 'quantity': 14},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'deathTrack', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'invincible', 'quantity': 1},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'victoryMarch', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'EFC2016', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'diehard', 'quantity': 1},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'WFC2014', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'tacticalBreakthrough', 'quantity': 0},
                             {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                              'achievement': 'handOfDeath', 'quantity': 1}]
        self.assertListEqual(response, expected_response)

    @responses.activate
    def test_load_in_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/arenas/',
            json=self.mock_tankopedia_maps(),
            status=200
        )
        wotapi = WotAPI(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            realm=self.test_realm,
            quietly=False,
            db_path=self.db_path,
            load_to_db=True,
            logging_enabled=True
        )
        wotapi.tankopedia_maps(load_to_db=True, load_once=True)
        result = self.db_loader.check_if_data_exists(model=TankopediaMapsModel)
        self.assertEqual(result, True)