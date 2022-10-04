import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.orm.data_model import TankopediaMapsModel
from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class TankopediaMapsData(BaseAction):

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

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, load_once: bool = False):
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm,
                                      source=APISource.tankopedia_maps)
        clean_data = self._parse_data(raw_data=raw_data)

        if load_to_db:
            db_loader = DBLoader(path=db_path)
            if load_once:
                # Checks if the data is already existing in the database else loads it.
                if db_loader.check_if_data_exists(TankopediaMapsModel):
                    logging.info('Tankopedia maps data will not be loaded into the database.')
                else:
                    db_loader.insert(TankopediaMapsModel, clean_data)
            else:
                db_loader.insert(TankopediaMapsModel, clean_data)

        return clean_data
