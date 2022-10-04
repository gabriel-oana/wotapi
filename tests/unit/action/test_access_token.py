import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.access_token import RenewAccessToken


class TestRenewAccessToken(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.POST,
            'https://api.worldoftanks.eu/wot/auth/prolongate/',
            json=self.mock_renew_access_token(),
            status=200
        )

        p = RenewAccessToken()
        data = p.etl_data(
            application_id=self.test_application_id,
            token=self.test_token,
            realm=self.test_realm,
        )

        expected_data = {'status': 'ok', 'meta': {'count': 3},
                         'data': {'access_token': '49a5800faeb33fcc49adb62dfbccc912b8694cec',
                                  'account_id': 'mock_account_id', 'expires_at': 1666035021}}

        self.assertDictEqual(data, expected_data)
