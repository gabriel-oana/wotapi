import requests
from wotapi.models.models import REALM, APISource


class RequestFactory:

    def __init__(self, application_id: str, realm: REALM, account_id: str = None, token: str = None,
                 source: APISource = APISource):
        self._account_id = account_id
        self._application_id = application_id
        self._access_token = token
        self._realm = realm
        self._source = source
        self._BASE_URL = 'https://api.worldoftanks.{}/wot'.format(realm)

    def prepare_request(self, nickname: str = None) -> requests.PreparedRequest:
        if self._source == APISource.account_id:
            prepped_request = self._get_account_id(nickname=nickname)
        elif self._source == APISource.renew_access_token:
            prepped_request = self._renew_access_token()
        elif self._source == APISource.player_achievements:
            prepped_request = self._player_achievements()
        elif self._source == APISource.player_personal_data:
            prepped_request = self._player_personal()
        elif self._source == APISource.player_vehicles_data:
            prepped_request = self._player_vehicles()
        elif self._source == APISource.tankopedia_achievements:
            prepped_request = self._tankopedia_achievements()
        elif self._source == APISource.tankopedia_badges:
            prepped_request = self._tankopedia_badges()
        elif self._source == APISource.tankopedia_info:
            prepped_request = self._tankopedia_information()
        elif self._source == APISource.tankopedia_maps:
            prepped_request = self._tankopedia_maps()
        elif self._source == APISource.tankopedia_vehicles:
            prepped_request = self._tankopedia_vehicles()
        elif self._source == APISource.vehicle_achievements:
            prepped_request = self._vehicle_achievements()
        elif self._source == APISource.vehicle_statistics:
            prepped_request = self._vehicle_statistics()
        else:
            raise ValueError('API Method invalid')

        return prepped_request

    @staticmethod
    def _prepare_request(url: str, method: str, params: dict = None, data: dict = None) -> requests.PreparedRequest:
        req = requests.Request(method, url=url, params=params, data=data)
        prepped_request = req.prepare()
        return prepped_request

    def _get_account_id(self, nickname: str) -> requests.PreparedRequest:
        """
        Gets the account id of a nickname
        """
        req = self._prepare_request(
            url="{}/account/list/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
                "search": nickname
            }
        )
        return req

    def _renew_access_token(self) -> requests.PreparedRequest:
        """
        Renews any access token
        """
        req = self._prepare_request(
            url="{}/auth/prolongate/".format(self._BASE_URL),
            method='POST',
            data={
                "application_id": self._application_id,
                "access_token": self._access_token
            }
        )
        return req

    def _vehicle_statistics(self) -> requests.PreparedRequest:
        """
        Extracts vehicles statistics in the player vehicle section.
        """
        req = self._prepare_request(
            url="{}/tanks/stats/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
                "access_token": self._access_token,
                "account_id": self._account_id
            }
        )
        return req

    def _vehicle_achievements(self) -> requests.PreparedRequest:
        """
        Extracts vehicles statistics in the player vehicle section.
        """
        req = self._prepare_request(
            url="{}/tanks/achievements/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
                "access_token": self._access_token,
                "account_id": self._account_id
            }
        )
        return req

    def _player_personal(self) -> requests.PreparedRequest:
        """
        Extracts player personal data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/account/info/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
                "access_token": self._access_token,
                "account_id": self._account_id
            }
        )
        return req

    def _player_vehicles(self) -> requests.PreparedRequest:
        """
        Extracts player vehicle data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/account/tanks/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
                "access_token": self._access_token,
                "account_id": self._account_id
            }
        )
        return req

    def _player_achievements(self) -> requests.PreparedRequest:
        """
        Extracts player achievements data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/account/achievements/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
                "account_id": self._account_id
            }
        )
        return req

    def _tankopedia_vehicles(self) -> requests.PreparedRequest:
        """
        Extracts tankopedia vehicles data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/encyclopedia/vehicles/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id
            }
        )
        return req

    def _tankopedia_achievements(self) -> requests.PreparedRequest:
        """
        Extracts tankopedia achievements data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/encyclopedia/achievements/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id
            }
        )
        return req

    def _tankopedia_information(self) -> requests.PreparedRequest:
        """
        Extracts tankopedia achievements data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/encyclopedia/info/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id
            }
        )
        return req

    def _tankopedia_maps(self) -> requests.PreparedRequest:
        """
        Extracts tankopedia achievements data from the accounts section.
        """
        req = self._prepare_request(
            url="{}/encyclopedia/arenas/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id
            }
        )
        return req

    def _tankopedia_badges(self) -> requests.PreparedRequest:
        """
        Extracts tankopedia badges.
        """
        req = self._prepare_request(
            url="{}/encyclopedia/badges/".format(self._BASE_URL),
            method='GET',
            params={
                "application_id": self._application_id,
            }
        )
        return req


