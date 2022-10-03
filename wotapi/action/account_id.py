import logging

from wotapi.utils.api import API
from wotapi.models.models import APISource


class AccountID:

    @staticmethod
    def _extract_data(application_id: str, realm: str, nickname: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Obtaining account id')

        wot = API(application_id=application_id, realm=realm)
        raw_data = wot.get_data(source=APISource.account_id, nickname=nickname)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict) -> str:
        return raw_data['data'][0]['account_id']

    def etl_data(self, application_id: str, realm: str, nickname: str) -> str:
        """
        Retrieves the account id for the user
        """
        raw_data = self._extract_data(application_id=application_id, realm=realm, nickname=nickname)
        account_id = self._parse_data(raw_data)
        return account_id