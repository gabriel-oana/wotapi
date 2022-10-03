import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import TankopediaBadgesModel
from wotapi.models.models import APISource


class TankopediaBadgesData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting tankopedia badges')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.tankopedia_badges)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts the tankopedia badges and formats it into a 2d format.
        """
        logging.info('Parsing tankopedia badges')

        badge_counter = raw_data['data'].keys()
        raw_data = raw_data['data']

        clean_data = []
        for i in badge_counter:
            temp_data = raw_data[str(i)]
            clean_data.append({
                "account_id": account_id,
                "badge_id": temp_data['badge_id'],
                "name": temp_data['name'],
                "description": temp_data['description'],
                "medium_icon": temp_data['images']['medium_icon'],
                "small_icon": temp_data['images']['small_icon'],
                "big_icon": temp_data['images']['big_icon']
            })

        return clean_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, realm: str, load_once: bool,
                 db_path: str) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            if load_once:
                # Checks if the data is already existing in the database else loads it.
                if DBLoader.check_if_data_exists(TankopediaBadgesModel, db_path=db_path):
                    logging.info('Tankopedia badge data will not be loaded into the database.')
                else:
                    DBLoader.insert(TankopediaBadgesModel, clean_data, db_path=db_path)
            else:
                DBLoader.insert(TankopediaBadgesModel, clean_data, db_path=db_path)

        return clean_data
