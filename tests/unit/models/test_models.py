import unittest
from wotapi.models.models import APISource, REALM


class TestModels(unittest.TestCase):

    def test_api_source_account_id(self):
        self.assertEqual(APISource.account_id, 'account_id')

    def test_api_source_renew_access_token(self):
        self.assertEqual(APISource.renew_access_token, 'renew_access_token')

    def test_api_source_player_achievements(self):
        self.assertEqual(APISource.player_achievements, 'player_achievements')

    def test_api_source_player_personal_data(self):
        self.assertEqual(APISource.player_personal_data, 'player_personal_data')

    def test_api_source_player_vehicles_data(self):
        self.assertEqual(APISource.player_vehicles_data, 'player_vehicles_data')

    def test_api_source_tankopedia_achievements(self):
        self.assertEqual(APISource.tankopedia_achievements, 'tankopedia_achievements')

    def test_api_source_tankopedia_badges(self):
        self.assertEqual(APISource.tankopedia_badges, 'tankopedia_badges')

    def test_api_source_tankopedia_info(self):
        self.assertEqual(APISource.tankopedia_info, 'tankopedia_info')

    def test_api_source_tankopedia_maps(self):
        self.assertEqual(APISource.tankopedia_maps, 'tankopedia_maps')

    def test_api_source_tankopedia_vehicles(self):
        self.assertEqual(APISource.tankopedia_vehicles, 'tankopedia_vehicles')

    def test_api_source_vehicle_achievements(self):
        self.assertEqual(APISource.vehicle_achievements, 'vehicle_achievements')

    def test_api_source_vehicle_statistics(self):
        self.assertEqual(APISource.vehicle_statistics, 'vehicle_statistics')

    def test_realms_eu(self):
        self.assertEqual(REALM.eu, 'eu')

    def test_realms_ru(self):
        self.assertEqual(REALM.ru, 'ru')

    def test_realms_na(self):
        self.assertEqual(REALM.na, 'na')

    def test_realms_asia(self):
        self.assertEqual(REALM.asia, 'asia')

