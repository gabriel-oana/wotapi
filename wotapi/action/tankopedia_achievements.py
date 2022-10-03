import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import TankopediaAchievementsModel
from wotapi.models.models import APISource


class TankopediaAchievementsData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player vehicles data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.tankopedia_achievements)

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player vehicles details data')

        # Get only the account data
        achievement_data = raw_data['data']

        clean_data = []
        for key, value in achievement_data.items():

            # TODO: Refactor this.
            # Some achievements have multiple options, others don't.
            if value['options']:
                for option in value['options']:
                    clean_data.append({
                        "name": option['name_i18n'],
                        "outdated": value['outdated'],
                        "section": value['section'],
                        "section_order": value['section_order'],
                        "image_big": option['image_big'],
                        "hero_info": value['hero_info'],
                        "name_i18n": value['name_i18n'],
                        "order": value['order'],
                        "type": value['type'],
                        "image": option['image'],
                        "condition": str(value['condition']).replace("•", ''),
                        "description": value['description']
                    })
            else:
                clean_data.append({
                    "name": value['name'],
                    "outdated": value['outdated'],
                    "section": value['section'],
                    "section_order": value['section_order'],
                    "image_big": value['image_big'],
                    "hero_info": value['hero_info'],
                    "name_i18n": value['name_i18n'],
                    "order": value['order'],
                    "type": value['type'],
                    "image": value['image'],
                    "condition": str(value['condition']).replace("•", ''),
                    "description": value['description']
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
                if DBLoader.check_if_data_exists(TankopediaAchievementsModel, db_path=db_path):
                    logging.info('Tankopedia achievements data will not be loaded into the database.')
                else:
                    DBLoader.insert(TankopediaAchievementsModel, clean_data, db_path=db_path)
            else:
                DBLoader.insert(TankopediaAchievementsModel, clean_data, db_path=db_path)

        return clean_data
