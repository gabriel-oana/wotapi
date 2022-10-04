import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.player_vehicles_data import PlayerVehiclesData
from wotapi.orm.data_model import PlayerPersonalVehiclesModel


class TestPlayerVehiclesData(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/tanks/',
            json=self.mock_response_vehicles_data(),
            status=200
        )

        p = PlayerVehiclesData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd()
        )

        expected_data = [{'tank_id': 8993, 'battles': 921, 'mark_of_mastery': 4, 'wins': 454},
                         {'tank_id': 54865, 'battles': 1, 'mark_of_mastery': 1, 'wins': 1}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/tanks/',
            json=self.mock_response_vehicles_data(),
            status=200
        )

        p = PlayerVehiclesData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path
        )

        data_exists = self.db_loader.check_if_data_exists(model=PlayerPersonalVehiclesModel)
        self.assertEqual(data_exists, True)
