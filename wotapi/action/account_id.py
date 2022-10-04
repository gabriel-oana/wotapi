from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class AccountID(BaseAction):

    @staticmethod
    def _parse_data(raw_data: dict) -> str:
        return raw_data['data'][0]['account_id']

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, nickname: str = None):
        """
        Retrieves the account id for the user
        """
        raw_data = self._extract_data(
            application_id=application_id,
            realm=realm,
            nickname=nickname,
            source=APISource.account_id
        )
        account_id = self._parse_data(raw_data)
        return account_id
