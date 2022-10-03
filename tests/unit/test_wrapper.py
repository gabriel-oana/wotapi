import os
import unittest
from wotapi.models.models import REALM
from wotapi.orm.data_model import DataModel
from wotapi.helper.db_loader import DBLoader
from wotapi.helper.create_engine import create_db_engine


class TestWrapper(unittest.TestCase):

    def setUp(self) -> None:
        self.test_account_id = 'mock_account_id'
        self.test_application_id = 'mock_application_id'
        self.test_token = 'mock_token'
        self.test_realm = REALM.eu

        self.db_path = f'tests'
        self.engine = create_db_engine(path=self.db_path)
        self.db_loader = DBLoader(db_engine=self.engine)
        DataModel.create_tables(engine=self.engine)

    @staticmethod
    def mock_renew_access_token(account_id: str) -> dict:
        response = {"status": "ok", "meta": {"count": 3},
                    "data": {"access_token": "49a5800faeb33fcc49adb62dfbccc912b8694cec", "account_id": account_id,
                             "expires_at": 1666035021}}
        return response

    @staticmethod
    def mock_account_id() -> dict:
        response = {"status": "ok", "meta": {"count": 1}, "data": [{"nickname": "mock-nickname", "account_id": 1}]}
        return response

    @staticmethod
    def mock_response_player_achievements(account_id: str) -> dict:
        response = {
            "status": "ok",
            "meta": {"count": 1},
            "data": {
                account_id: {
                    "achievements": {
                        "medalCarius": 1,
                    },
                    "frags": {
                        "crucialShotMedal": 3
                    },
                    "max_series": {
                        "armorPiercer": 23
                    }
                }
            }
        }

        return response

    def tearDown(self) -> None:
        os.remove(self.db_path + '/world_of_tanks.db')
