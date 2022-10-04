import os
import responses
from tests.unit.test_wrapper import TestWrapper
from wotapi.action.player_achievements import PlayerAchievementsData
from wotapi.orm.data_model import PlayerAchievementsModel


class TestPlayerAchievements(TestWrapper):

    @responses.activate
    def test_etl_data(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/achievements/',
            json=self.mock_response_player_achievements(),
            status=200
        )

        p = PlayerAchievementsData()
        data = p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=False,
            realm=self.test_realm,
            db_path=os.getcwd()
        )

        expected_data = [{'medal_type': 'achievements', 'medal_name': 'medalCarius', 'medal_quantity': 1},
                         {'medal_type': 'frags', 'medal_name': 'crucialShotMedal', 'medal_quantity': 3},
                         {'medal_type': 'max_series', 'medal_name': 'armorPiercer', 'medal_quantity': 23}]

        self.assertListEqual(data, expected_data)

    @responses.activate
    def test_etl_data_loading_into_db(self):
        responses.add(
            responses.GET,
            'https://api.worldoftanks.eu/wot/account/achievements/',
            json=self.mock_response_player_achievements(),
            status=200
        )

        p = PlayerAchievementsData()
        p.etl_data(
            application_id=self.test_application_id,
            account_id=self.test_account_id,
            token=self.test_token,
            load_to_db=True,
            realm=self.test_realm,
            db_path=self.db_path
        )

        data_exists = self.db_loader.check_if_data_exists(model=PlayerAchievementsModel)
        self.assertEqual(data_exists, True)


