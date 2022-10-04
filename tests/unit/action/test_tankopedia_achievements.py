import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.tankopedia_achievements import TankopediaAchievementsData
from wotapi.orm.data_model import TankopediaAchievementsModel


class TestTankopediaAchievementsData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/achievements/',
            json=self.mock_tankopedia_achievements(),
            status=200
        )

        p = TankopediaAchievementsData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd(),
            load_once=False
        )
        expected_data = [{'name': 'crucialShotMedal', 'outdated': False, 'section': 'special', 'section_order': 1,
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

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/achievements/',
            json=self.mock_tankopedia_achievements(),
            status=200
        )

        p = TankopediaAchievementsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaAchievementsModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_already_exists(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/achievements/',
            json=self.mock_tankopedia_achievements(),
            status=200
        )

        p = TankopediaAchievementsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        # Just run it twice.
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaAchievementsModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_multiple_times(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/achievements/',
            json=self.mock_tankopedia_achievements(),
            status=200
        )

        p = TankopediaAchievementsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=False
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaAchievementsModel)
        self.assertEqual(data_exists, True)
