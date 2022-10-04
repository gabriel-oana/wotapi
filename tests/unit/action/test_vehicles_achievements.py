import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.vehicles_achievements import VehicleAchievementsData
from wotapi.orm.data_model import VehiclesAchievementsModel


class TestVehiclesAchievements(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/tanks/achievements/',
            json=self.mock_response_vehicles_achievements(),
            status=200
        )

        p = VehicleAchievementsData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd()
        )
        print(data)
        expected_data = [{'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                          'achievement': 'medalCarius', 'quantity': 4},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                          'achievement': 'titleSniper', 'quantity': 14},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                          'achievement': 'markOfMastery', 'quantity': 1},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'achievements',
                          'achievement': 'armorPiercer', 'quantity': 14},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'armorPiercer', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'aimer', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'titleSniper', 'quantity': 10},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'deathTrack', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'invincible', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'victoryMarch', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'EFC2016', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'diehard', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'WFC2014', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'tacticalBreakthrough', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'series',
                          'achievement': 'handOfDeath', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'armorPiercer', 'quantity': 14},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'aimer', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'titleSniper', 'quantity': 14},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'deathTrack', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'invincible', 'quantity': 1},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'victoryMarch', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'EFC2016', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'diehard', 'quantity': 1},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'WFC2014', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'tacticalBreakthrough', 'quantity': 0},
                         {'account_id': 'mock_account_id', 'tank_id': 8257, 'achievement_type': 'max_series',
                          'achievement': 'handOfDeath', 'quantity': 1}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/tanks/achievements/',
            json=self.mock_response_vehicles_achievements(),
            status=200
        )

        p = VehicleAchievementsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path
        )

        data_exists = self.db_loader.check_if_data_exists(model=VehiclesAchievementsModel)
        self.assertEqual(data_exists, True)
