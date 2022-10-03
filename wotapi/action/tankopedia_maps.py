import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import TankopediaMapsModel
from wotapi.models.models import APISource


class TankopediaMapsData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting tankopedia maps data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.tankopedia_maps)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing tankopedia maps details data')

        # Get only the account data
        map_data = raw_data['data']

        clean_data = []

        for key, value in map_data.items():
            clean_data.append({
                "name": value['name_i18n'],
                "camouflage_type": value['camouflage_type'],
                "description": value['description'],
                "arena_id": value['arena_id']
            })

        return clean_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, load_once: bool,
                 realm: str, db_path: str) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        clean_data = self._parse_data(raw_data=raw_data)

        if load_to_db:
            if load_once:
                # Checks if the data is already existing in the database else loads it.
                if DBLoader.check_if_data_exists(TankopediaMapsModel, db_path=db_path):
                    logging.info('Tankopedia maps data will not be loaded into the database.')
                else:
                    DBLoader.insert(TankopediaMapsModel, clean_data, db_path=db_path)
            else:
                DBLoader.insert(TankopediaMapsModel, clean_data, db_path=db_path)

        return clean_data
