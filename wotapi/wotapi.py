import os

from wotapi.helper.validators import Validators
from wotapi.helper.create_engine import create_db_engine
from wotapi.helper.logger import create_logger
from wotapi.orm.data_model import DataModel
from wotapi.action.account_id import AccountID
from wotapi.action.access_token import RenewAccessToken
from wotapi.action.player_personal_data import PlayerPersonalData
from wotapi.action.player_vehicles_data import PlayerVehiclesData
from wotapi.action.player_achievements import PlayerAchievementsData
from wotapi.action.tankopedia_vehicles import TankopediaVehiclesData
from wotapi.action.tankopedia_achievements import TankopediaAchievementsData
from wotapi.action.tankopedia_info import TankopediaInfoData
from wotapi.action.tankopedia_maps import TankopediaMapsData
from wotapi.action.tankopedia_badges import TankopediaBadgesData
from wotapi.action.vehicles_statistics import VehicleStatisticsData
from wotapi.action.vehicles_achievements import VehicleAchievementsData


class WotAPI:

    def __init__(self, application_id: str, account_id: str, token: str, realm: str, quietly: bool = True,
                 logging_enabled: bool = False, log_level: str = "WARNING", load_to_db: bool = True,
                 db_path: str = os.getcwd()):
        if logging_enabled:
            self.log_level = create_logger(log_level)
        self.quietly = quietly
        self.application_id = application_id
        self.account_id = account_id
        self.token = token
        self.realm = realm
        self.load_to_db = load_to_db
        self.db_path = db_path

        if self.load_to_db:
            """
            Create the database at the declared path. 
            """
            engine = create_db_engine(path=self.db_path)
            DataModel.create_tables(engine=engine)
            if not self.quietly:
                print('Database created')

    def _check_parameters(self):
        """
        Validates if the application id, account_id and token exist.
        """
        Validators.check_if_param_exists(self.token, 'token')
        Validators.check_if_param_exists(self.account_id, 'account_id')
        Validators.check_if_param_exists(self.application_id, 'application_id')
        Validators.check_realm(self.realm)

    def get_account_id(self, nickname: str) -> str:
        """
        Retrieves the account id
        """
        account = AccountID()
        data = account.etl_data(application_id=self.application_id,
                                realm=self.realm,
                                nickname=nickname)
        return data

    def renew_token(self) -> dict:
        """
        Retrieves the account id
        """
        account = RenewAccessToken()
        data = account.etl_data(application_id=self.application_id,
                                realm=self.realm,
                                token=self.token)
        return data

    def player_personal(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of personal data into the database.
        Requires a personal access token.
        """

        self._check_parameters()

        personal_data = PlayerPersonalData()
        data = personal_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print('Player personal data has been extracted')

        return data

    def player_vehicles(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of player vehicle data into the database.
        Requires a personal access token.
        """
        self._check_parameters()

        vehicles_data = PlayerVehiclesData()
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Player personal vehicles data has been extracted")
        return data

    def player_achievements(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of player achievements data into the database.
        Requires a personal access token.
        """
        self._check_parameters()

        vehicles_data = PlayerAchievementsData()
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Player personal achievements data has been extracted")
        return data

    def tankopedia_vehicles(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia vehicles data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaVehiclesData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia vehicles data has been extracted")
        return data

    def tankopedia_achievements(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia achievements data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaAchievementsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia achievements has been extracted")
        return data

    def tankopedia_information(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia information data into the database.
        """
        self._check_parameters()

        info = TankopediaInfoData()
        data = info.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                             load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia information has been extracted")
        return data

    def tankopedia_maps(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia maps data into the database.
        """
        self._check_parameters()

        info = TankopediaMapsData()
        data = info.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                             load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia maps has been extracted")
        return data

    def tankopedia_badges(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of vehicle statistics data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaBadgesData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, realm=self.realm, load_once=load_once, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia badges have been extracted")
        return data

    def vehicle_statistics(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of vehicle statistics data into the database.
        """
        self._check_parameters()

        vehicles = VehicleStatisticsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Vehicle statistics has been extracted")
        return data

    def vehicle_achievements(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of vehicle statistics data into the database.
        """
        self._check_parameters()

        vehicles = VehicleAchievementsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Vehicle achievements has been extracted")
        return data

