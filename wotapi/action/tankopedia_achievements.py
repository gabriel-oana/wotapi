import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.orm.data_model import TankopediaAchievementsModel
from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class TankopediaAchievementsData(BaseAction):

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

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, load_once: bool = False):
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
            source=APISource.tankopedia_achievements
        )
        clean_data = self._parse_data(raw_data=raw_data)

        if load_to_db:
            db_loader = DBLoader(path=db_path)

            if load_once:
                # Checks if the data is already existing in the database else loads it.
                if db_loader.check_if_data_exists(TankopediaAchievementsModel):
                    logging.info('Tankopedia achievements data will not be loaded into the database.')
                else:
                    db_loader.insert(TankopediaAchievementsModel, clean_data)
            else:
                db_loader.insert(TankopediaAchievementsModel, clean_data)

        return clean_data
