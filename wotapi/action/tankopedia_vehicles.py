import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import TankopediaVehiclesModel
from wotapi.models.models import APISource


class TankopediaVehiclesData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player vehicles data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.tankopedia_vehicles)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player vehicles details data')

        # Get only the account data
        tank_data = raw_data['data']

        clean_data = []
        for key, value in tank_data.items():
            clean_data.append({
                "tank_id": value['tank_id'],
                "is_wheeled": value['is_wheeled'],
                "is_premium": value['is_premium'],
                "tag": value['tag'],
                "small_icon": value['images']['small_icon'],
                "contour_icon": value['images']['contour_icon'],
                "big_icon": value['images']['big_icon'],
                "type": value['type'],
                "description": value['description'],
                "short_name": value['short_name'],
                "nation": value['nation'],
                "tier": value['tier'],
                "is_gift": value['is_gift'],
                "name": value['name'],
                "price_gold": value['price_gold'],
                "price_credit": value['price_credit']
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
                if DBLoader.check_if_data_exists(TankopediaVehiclesModel, db_path=db_path):
                    logging.info('Tankopedia vehicles data will not be loaded into the database.')
                else:
                    DBLoader.insert(TankopediaVehiclesModel, clean_data, db_path=db_path)
            else:
                DBLoader.insert(TankopediaVehiclesModel, clean_data, db_path=db_path)

        return clean_data
