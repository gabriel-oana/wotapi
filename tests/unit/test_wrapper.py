import os
import json
import unittest
from wotapi.models.models import REALM
from wotapi.orm.data_model import DataModel
from wotapi.helper.db_loader import DBLoader
from wotapi.helper.create_engine import create_db_engine


class TestWrapper(unittest.TestCase):

    def setUp(self) -> None:
        self.test_account_id = 'mock_account_id'
        self.test_application_id = 'mock_application_id'
        self.test_token = 'mock_token'
        self.test_realm = REALM.eu

        self.db_path = 'tests'
        self.engine = create_db_engine(path=self.db_path)
        self.db_loader = DBLoader(db_engine=self.engine)
        DataModel.create_tables(engine=self.engine)

    @staticmethod
    def _get_data_file(file_name: str):
        """
        Loads the JSON file with the sample data required for the tests.
        """
        with open(f'tests/files/{file_name}', 'r') as f:
            data = json.loads(f.read())

        return data

    def mock_renew_access_token(self) -> dict:
        return self._get_data_file('renew_access_token.json')

    def mock_account_id(self) -> dict:
        return self._get_data_file('account_id.json')

    def mock_response_player_achievements(self) -> dict:
        return self._get_data_file('player_achievements.json')

    def mock_response_player_personal(self):
        return self._get_data_file('player_personal_data.json')

    def mock_response_vehicles_data(self):
        return self._get_data_file('player_vehicles_data.json')

    def mock_tankopedia_achievements(self):
        return self._get_data_file('tankopedia_achievements.json')

    def mock_tankopedia_badges(self):
        return self._get_data_file('tankopedia_badges.json')

    def mock_tankopedia_info(self):
        return self._get_data_file('tankopedia_info.json')

    def mock_tankopedia_maps(self):
        return self._get_data_file('tankopedia_maps.json')

    def mock_tankopedia_vehicles(self):
        return self._get_data_file('tankopedia_vehicles.json')

    def mock_response_vehicles_achievements(self):
        return self._get_data_file('vehicles_achievements.json')

    def mock_response_vehicles_statistics(self):
        return self._get_data_file('vehicles_statistics.json')

    def tearDown(self) -> None:
        os.remove(self.db_path + '/world_of_tanks.db')
