import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.tankopedia_vehicles import TankopediaVehiclesData
from wotapi.orm.data_model import TankopediaVehiclesModel


class TestTankopediaVehiclesData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/',
            json=self.mock_tankopedia_vehicles(),
            status=200
        )

        p = TankopediaVehiclesData()
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
        expected_data = [{'tank_id': 1, 'is_wheeled': False, 'is_premium': False, 'tag': 'R04_T-34',
                          'small_icon': 'http:\\/\\/api.worldoftanks.eu\\/static\\/2.71.0\\/wot\\/encyclopedia\\/vehicle\\/small\\/ussr-R04_T-34.png',
                          'contour_icon': 'http:\\/\\/api.worldoftanks.eu\\/static\\/2.71.0\\/wot\\/encyclopedia\\/vehicle\\/contour\\/ussr-R04_T-34.png',
                          'big_icon': 'http:\\/\\/api.worldoftanks.eu\\/static\\/2.71.0\\/wot\\/encyclopedia\\/vehicle\\/ussr-R04_T-34.png',
                          'type': 'mediumTank',
                          'description': 'The legend of the Soviet armored forces and the most widely-produced Soviet tank of World War II, with a total of 33,805 vehicles manufactured. Three variants of this model were produced at several Soviet factories from 1940 through 1944.',
                          'short_name': 'T-34', 'nation': 'ussr', 'tier': 5, 'is_gift': False, 'name': 'T-34',
                          'price_gold': 0, 'price_credit': 356700}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/',
            json=self.mock_tankopedia_vehicles(),
            status=200
        )

        p = TankopediaVehiclesData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=True
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaVehiclesModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_already_exists(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/',
            json=self.mock_tankopedia_vehicles(),
            status=200
        )

        p = TankopediaVehiclesData()
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

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaVehiclesModel)
        self.assertEqual(data_exists, True)

    @responses.activate
    def test_etl_data_loading_into_db_multiple_times(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/',
            json=self.mock_tankopedia_vehicles(),
            status=200
        )

        p = TankopediaVehiclesData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path,
            load_once=False
        )

        data_exists = self.db_loader.check_if_data_exists(model=TankopediaVehiclesModel)
        self.assertEqual(data_exists, True)
