import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.orm.data_model import TankopediaBadgesModel
from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class TankopediaBadgesData(BaseAction):

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

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, load_once: bool = False):
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm,
                                      source=APISource.tankopedia_badges)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            db_loader = DBLoader(path=db_path)
            if load_once:
                # Checks if the data is already existing in the database else loads it.
                if db_loader.check_if_data_exists(TankopediaBadgesModel):
                    logging.info('Tankopedia badge data will not be loaded into the database.')
                else:
                    db_loader.insert(TankopediaBadgesModel, clean_data)
            else:
                db_loader.insert(TankopediaBadgesModel, clean_data)

        return clean_data
