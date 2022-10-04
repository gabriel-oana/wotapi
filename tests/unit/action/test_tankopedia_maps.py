import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.tankopedia_maps import TankopediaMapsData
from wotapi.orm.data_model import TankopediaMapsModel


class TestTankopediaMapsData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/arenas/',
            json=self.mock_tankopedia_maps(),
            status=200
        )

        p = TankopediaMapsData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd(),
            load_once=False
        )
        print(data)
        expected_data = [{'name': 'Ruinberg', 'camouflage_type': 'summer', 'description': 'Some description',
                          'arena_id': '08_ruinberg'}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/arenas/',
            json=self.mock_tankopedia_maps(),
            status=200
        )

        p = TankopediaMapsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaMapsModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_already_exists(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/arenas/',
            json=self.mock_tankopedia_maps(),
            status=200
        )

        p = TankopediaMapsData()
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

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaMapsModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_multiple_times(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/arenas/',
            json=self.mock_tankopedia_maps(),
            status=200
        )

        p = TankopediaMapsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=False
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaMapsModel)
        self.assertEqual(data_exists, True)
