import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.account_id import AccountID


class TestAccountID(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/list/',
            json=self.mock_account_id(),
            status=200
        )

        p = AccountID()
        data = p.etl_data(
            application_id=self.test_application_id,
            nickname='test-nickname',
            realm=self.test_realm,
        )

        self.assertEqual(data, 1)
