import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.orm.data_model import VehiclesAchievementsModel
from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class VehicleAchievementsData(BaseAction):

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

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, load_once: bool = False):
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm,
                                      source=APISource.vehicle_achievements)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            db_loader = DBLoader(path=db_path)
            db_loader.insert(VehiclesAchievementsModel, clean_data)

        return clean_data
