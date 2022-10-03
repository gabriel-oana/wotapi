import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import VehiclesStatisticsModel, VehiclesFragsModel
from wotapi.models.models import APISource


class VehicleStatisticsData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player vehicles data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.vehicle_statistics)

        return raw_data

    @staticmethod
    def _parse_vehicle_statistics(raw_data: dict, account_id: str) -> list:
        """
        Extracts the vehicle statistics data and formats it to fit the database.
        """
        logging.info('Parsing vehicle statistics data')

        raw_data = raw_data['data'][account_id]
        statistic_data = []
        for i in range(0, len(raw_data)):

            temp_data = raw_data[i]
            battle_types = ['clan', 'all', 'regular_team', 'company', 'stronghold_skirmish', 'stronghold_defense',
                            'globalmap', 'team']

            for battle_type in battle_types:
                account_data = temp_data[battle_type]

                statistic_data.append({
                    "account_id": account_id,
                    "battle_type": battle_type,
                    "spotted": account_data.get('spotted', None),
                    "battles_on_stunning_vehicles":  account_data.get('battles_on_stunning_vehicles', None),
                    "max_xp": temp_data['max_xp'],
                    "xp": account_data.get('xp', None),
                    "survived_battles": account_data.get('survived_battles', None),
                    "dropped_capture_points": account_data.get('dropped_capture_points', None),
                    "hits_percents": account_data.get('hits_percents', None),
                    "draws": account_data.get('draws', None),
                    "battles": account_data.get('battles', None),
                    "damage_received": account_data.get('damage_received', None),
                    "frags": account_data.get('frags', None),
                    "stun_number": account_data.get('stun_number', None),
                    "capture_points": account_data.get('capture_points', None),
                    "stun_assisted_damage": account_data.get('stun_assisted_damage', None),
                    "max_damage": account_data.get('max_damage', None),
                    "hits": account_data.get('hits', None),
                    "battle_avg_xp": account_data.get('battle_avg_xp', None),
                    "wins": account_data.get('wins', None),
                    "losses": account_data.get('losses', None),
                    "damage_dealt": account_data.get('damage_dealt', None),
                    "max_frags": temp_data['max_frags'],
                    "shots": account_data.get('shots', None),
                    "direct_hits_received": account_data.get('direct_hits_received', None),
                    "explosion_hits": account_data.get('explosion_hits', None),
                    "piercings_received": account_data.get('piercings_received', None),
                    "piercings": account_data.get('piercings', None),
                    "no_damage_direct_hits_received": account_data.get('no_damage_direct_hits_received', None),
                    "explosion_hits_received": account_data.get('explosion_hits_received', None),
                    "tanking_factor": account_data.get('tanking_factor', None),
                    "avg_damage_blocked": account_data.get('avg_damage_blocked', None),
                    "mark_of_mastery": temp_data['mark_of_mastery'],
                    "in_garage": temp_data['in_garage'],
                    "tank_id": temp_data['tank_id'],
                })

        return statistic_data

    @staticmethod
    def _parse_vehicle_frags(raw_data: dict, account_id: str) -> list:
        """
        Extracts the vehicle frags and formats it into a 2d format.
        """
        logging.info('Parsing vehicle statistics data')

        raw_data = raw_data['data'][account_id]
        frags_data = []
        for i in range(0, len(raw_data)):

            temp_data = raw_data[i]
            for key, value in temp_data['frags'].items():
                frags_data.append({
                    "account_id": account_id,
                    "tank_id": temp_data['tank_id'],
                    "opponent_tank_id": key,
                    "frags": value
                })

        return frags_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, realm: str,
                 db_path: str) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        statistics_data = self._parse_vehicle_statistics(raw_data=raw_data, account_id=account_id)
        frags_data = self._parse_vehicle_frags(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            DBLoader.insert(VehiclesStatisticsModel, statistics_data, db_path=db_path)
            DBLoader.insert(VehiclesFragsModel, frags_data, db_path=db_path)

        clean_data = [{
            "statistics_data": statistics_data,
            "frags_data": frags_data
        }]

        return clean_data
