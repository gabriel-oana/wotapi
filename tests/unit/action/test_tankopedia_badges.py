import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.tankopedia_badges import TankopediaBadgesData
from wotapi.orm.data_model import TankopediaBadgesModel


class TestTankopediaBadgesData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/badges/',
            json=self.mock_tankopedia_badges(),
            status=200
        )

        p = TankopediaBadgesData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd(),
            load_once=False
        )

        expected_data = [{'account_id': 'mock_account_id', 'badge_id': 1, 'name': 'Gold, Beta Season',
                          'description': 'Reach League I in Beta Season of the Ranked Battle mode.',
                          'medium_icon': 'http://badge_1.png', 'small_icon': 'http://badge_1.png',
                          'big_icon': 'http://badge_1.png'}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/badges/',
            json=self.mock_tankopedia_badges(),
            status=200
        )

        p = TankopediaBadgesData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaBadgesModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_already_exists(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/badges/',
            json=self.mock_tankopedia_badges(),
            status=200
        )

        p = TankopediaBadgesData()
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

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaBadgesModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_multiple_times(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/badges/',
            json=self.mock_tankopedia_badges(),
            status=200
        )

        p = TankopediaBadgesData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=False
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaBadgesModel)
        self.assertEqual(data_exists, True)
