import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import VehiclesAchievementsModel
from wotapi.models.models import APISource


class VehicleAchievementsData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting vehicle achievements')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.vehicle_achievements)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts the vehicle achievements and formats it into a 2d format.
        """
        logging.info('Parsing vehicle achievements data')

        raw_data = raw_data['data'][account_id]
        clean_data = []
        for i in range(0, len(raw_data)):
            temp_data = raw_data[i]
            achievement_types = ['achievements', 'series', 'max_series']

            for achievement in achievement_types:
                for key, value in temp_data[achievement].items():
                    clean_data.append({
                        "account_id": account_id,
                        "tank_id": temp_data['tank_id'],
                        "achievement_type": achievement,
                        "achievement": key,
                        "quantity": value
                    })

        return clean_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, realm: str,
                 db_path: str) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            DBLoader.insert(VehiclesAchievementsModel, clean_data, db_path=db_path)

        return clean_data
