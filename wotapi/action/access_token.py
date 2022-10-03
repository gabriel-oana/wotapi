import logging

from wotapi.utils.api import API
from wotapi.models.models import APISource


class RenewAccessToken:

    @staticmethod
    def _extract_data(application_id: str, realm: str, token: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Obtaining account id')

        wot = API(application_id=application_id, realm=realm, token=token)
        raw_data = wot.get_data(source=APISource.renew_access_token)

        return raw_data

    def etl_data(self, application_id: str, token: str, realm: str) -> dict:
        """
        Retrieves the account id for the user
        """
        raw_data = self._extract_data(application_id=application_id, realm=realm, token=token)
        return raw_data
