import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.tankopedia_info import TankopediaInfoData
from wotapi.orm.data_model import TankopediaInfoModel


class TestTankopediaInfoData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/info/',
            json=self.mock_tankopedia_info(),
            status=200
        )

        p = TankopediaInfoData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd(),
            load_once=False
        )

        expected_data = [{'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'loader', 'value': 'Loader'},
                         {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'radioman',
                          'value': 'Radio Operator'},
                         {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'driver', 'value': 'Driver'},
                         {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'gunner', 'value': 'Gunner'},
                         {'metric': 'vehicle_crew_roles', 'group': None, 'alias': 'commander', 'value': 'Commander'},
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
                         {'metric': 'achievement_sections', 'group': 'battle', 'alias': 'Battle Heroes', 'value': 0},
                         {'metric': 'achievement_sections', 'group': 'epic', 'alias': 'Epic Medals', 'value': 2},
                         {'metric': 'achievement_sections', 'group': 'class', 'alias': 'Stage Awards', 'value': 5},
                         {'metric': 'achievement_sections', 'group': 'special', 'alias': 'Honorary Ranks', 'value': 1}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/info/',
            json=self.mock_tankopedia_info(),
            status=200
        )

        p = TankopediaInfoData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaInfoModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_already_exists(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/info/',
            json=self.mock_tankopedia_info(),
            status=200
        )

        p = TankopediaInfoData()
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

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaInfoModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_multiple_times(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/info/',
            json=self.mock_tankopedia_info(),
            status=200
        )

        p = TankopediaInfoData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=False
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaInfoModel)
        self.assertEqual(data_exists, True)
