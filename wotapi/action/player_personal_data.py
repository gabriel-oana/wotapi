import logging

from wotapi.helper.db_loader import DBLoader
from wotapi.utils.api import API
from wotapi.orm.data_model import PlayerPersonalDataStatisticsModel, PlayerPersonalDataDetailsModel
from wotapi.models.models import APISource


class PlayerPersonalData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player personal data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source=APISource.player_personal_data)

        return raw_data

    @staticmethod
    def _parse_details_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player personal details data')
        # Get only the account data
        account_data = raw_data['data'][account_id]

        details_data = [{
            "account_id": account_id,
            "last_battle_time": account_data.get('last_battle_time', None),
            "created_at": account_data['created_at'],
            "updated_at": account_data['updated_at'],
            "gold": account_data['private']['gold'],
            "free_xp": account_data['private']['free_xp'],
            "ban_time": account_data['private']['ban_time'],
            "is_bound_to_phone": account_data['private']['is_bound_to_phone'],
            "is_premium": account_data['private']['is_premium'],
            "credits": account_data['private']['credits'],
            "premium_expires_at": account_data['private']['premium_expires_at'],
            "bonds": account_data['private']['bonds'],
            "battle_life_time": account_data['private']['battle_life_time'],
            "global_rating": account_data['global_rating'],
            "clan_id": account_data['clan_id']
        }]

        return details_data

    @staticmethod
    def _parse_statistics_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the statistics data.
        The data is composed of four records based on the statistic type.
        """
        logging.info('Parsing player personal statistics data')

        raw_data = raw_data['data'][account_id]['statistics']
        statistic_types = ['clan', 'all', 'regular_team', 'company', 'stronghold_skirmish', 'stronghold_defense',
                           'historical', 'team']

        statistic_data = []
        for statistic_type in statistic_types:
            account_data = raw_data[statistic_type]
            statistic_data.append({
                "statistic_type": statistic_type,
                "spotted": account_data['spotted'],
                "battles_on_stunning_vehicles": account_data['battles_on_stunning_vehicles'],
                "avg_damage_blocked": account_data.get("avg_damage_blocked", None),
                "direct_hits_received": account_data['direct_hits_received'],
                "explosion_hits": account_data['explosion_hits'],
                "piercings_received": account_data['piercings_received'],
                "piercings": account_data['piercings'],
                "max_damage_tank_id": account_data.get("max_damage_tank_id", None),
                "xp": account_data['xp'],
                "survived_battles": account_data['survived_battles'],
                "dropped_capture_points": account_data['dropped_capture_points'],
                "hits_percents": account_data['hits_percents'],
                "draws": account_data['draws'],
                "max_xp_tank_id": account_data.get("max_xp_tank_id", None),
                "battles": account_data['battles'],
                "damage_received": account_data['damage_received'],
                "avg_damage_assisted": account_data.get("avg_damage_assisted", None),
                "max_frags_tank_id": account_data.get("max_frags_tank_id", None),
                "avg_damage_assisted_track": account_data.get("avg_damage_assisted_track", None),
                "frags": account_data['frags'],
                "stun_number": account_data['stun_number'],
                "avg_damage_assisted_radio": account_data.get("avg_damage_assisted_radio", None),
                "capture_points": account_data['capture_points'],
                "stun_assisted_damage": account_data['stun_assisted_damage'],
                "max_damage": account_data.get("max_damage", None),
                "hits": account_data['hits'],
                "battle_avg_xp": account_data['battle_avg_xp'],
                "wins": account_data['wins'],
                "losses": account_data['losses'],
                "damage_dealt": account_data['damage_dealt'],
                "no_damage_direct_hits_received": account_data['no_damage_direct_hits_received'],
                "max_frags": account_data.get("max_frags", None),
                "shots": account_data['shots'],
                "explosion_hits_received": account_data['explosion_hits_received'],
                "tanking_factor": account_data['tanking_factor']
            })

        return statistic_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, realm: str, db_path: str) \
            -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        details = self._parse_details_data(raw_data, account_id=account_id)
        statistics = self._parse_statistics_data(raw_data, account_id=account_id)

        if load_to_db:
            db_loader = DBLoader(path=db_path)
            db_loader.insert(PlayerPersonalDataDetailsModel, details)
            db_loader.insert(PlayerPersonalDataStatisticsModel, statistics)

        # Return the dict with combined data
        result = [{
            "details": details,
            "statistics": statistics
        }]

        return result
