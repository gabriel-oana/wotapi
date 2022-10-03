import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import PlayerAchievementsModel
from wotapi.models.models import APISource


class PlayerAchievementsData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player achivements data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.player_achievements)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player achievements data')

        # Get only the account data
        account_data = raw_data['data'][account_id]

        clean_data = []
        for medal_type in ['achievements', 'frags', 'max_series']:
            for key, value in account_data[medal_type].items():
                clean_data.append({
                    "medal_type": medal_type,
                    "medal_name": key,
                    "medal_quantity": value
                })

        return clean_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, realm: str, db_path: str) \
            -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            db_loader = DBLoader(path=db_path)
            db_loader.insert(PlayerAchievementsModel, clean_data)

        return clean_data
