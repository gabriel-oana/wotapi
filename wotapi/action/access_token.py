from wotapi.models.models import APISource, REALM
from wotapi.action.base_action import BaseAction


class RenewAccessToken(BaseAction):

    def etl_data(self, application_id: str, account_id: str = None, token: str = None,
                 realm: REALM = None, load_to_db: bool = False, db_path: str = None, **kwargs) -> dict:
        """
        Retrieves the account id for the user
        """
        raw_data = self._extract_data(
            application_id=application_id,
            realm=realm,
            token=token,
            source=APISource.renew_access_token
        )
        return raw_data
