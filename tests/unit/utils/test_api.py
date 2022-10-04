import responses
import requests

from tests.unit.test_wrapper import TestWrapper
from wotapi.models.models import REALM, APISource
from wotapi.utils.api import API


class TestAPI(TestWrapper):

    @responses.activate
    def test_get_data_is_success(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/list/',
            json=self.mock_account_id(),
            status=200
        )

        api = API()
        data = api.get_data(
            account_id=None,
            application_id=self.test_application_id,
            token=None,
            realm=REALM.eu,
            source=APISource.account_id,
            nickname='test-user'
        )
        expected_response = {'status': 'ok', 'meta': {'count': 1},
                             'data': [{'nickname': 'mock-nickname', 'account_id': 1}]}
        self.assertDictEqual(data, expected_response)

    @responses.activate
    def test_get_data_server_error_raises(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/list/',
            json={"success": False},
            status=500
        )
        api = API(
            max_attempts=2,
            backoff_multiplier=0
        )
        self.assertRaises(requests.exceptions.HTTPError, api.get_data, application_id=self.test_application_id,
                          source=APISource.account_id, realm=REALM.eu)

    def test_get_data_wrong_source_raises(self):
        api = API(
            max_attempts=2,
            backoff_multiplier=0
        )
        self.assertRaises(ValueError, api.get_data, application_id=self.test_application_id,
                          source='random-source', realm=REALM.eu)
