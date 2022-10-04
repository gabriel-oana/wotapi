import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.orm.data_model import PlayerPersonalVehiclesModel
from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class PlayerVehiclesData(BaseAction):

    @staticmethod
    def _parse_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player vehicles details data')

        # Get only the account data
        account_data = raw_data['data'][account_id]

        clean_data = []
        for item in account_data:
            clean_data.append({
                "tank_id": item['tank_id'],
                "battles": item['statistics']['battles'],
                "mark_of_mastery": item['mark_of_mastery'],
                "wins": item['statistics']['wins']
            })

        return clean_data

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, **kwargs):
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(
            account_id=account_id,
            application_id=application_id,
            token=token,
            realm=realm,
            source=APISource.player_vehicles_data
        )
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            db_loader = DBLoader(path=db_path)
            db_loader.insert(PlayerPersonalVehiclesModel, clean_data)

        return clean_data
