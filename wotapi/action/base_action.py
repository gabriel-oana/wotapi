import logging
from abc import ABC, abstractmethod

from wotapi.models.models import REALM, APISource
from wotapi.utils.api import API


class BaseAction(ABC):

    @abstractmethod
    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, **kwargs):
        raise NotImplementedError

    @staticmethod
    def _extract_data(application_id: str, source: APISource, account_id: str = None, token: str = None,
                      realm: REALM = None, nickname: str = None) -> dict:
        """
        Extracts Data from the api
        """

        logging.info(f'Extracting from {source}')

        wot = API()
        raw_data = wot.get_data(
            application_id=application_id,
            account_id=account_id,
            token=token,
            realm=realm,
            source=source,
            nickname=nickname
        )

        return raw_data
