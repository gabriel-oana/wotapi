import logging
import time

import requests
from requests import Session
from wotapi.utils.request_factory import RequestFactory
from wotapi.models.models import REALM, APISource


class API:

    def __init__(self, max_attempts: int = 3, backoff_multiplier: int = 10):
        self.MAX_ATTEMPTS = max_attempts
        self.BACKOFF_MULTIPLIER = backoff_multiplier
        self.status_codes_to_retry = [429, 500]
        self.status_codes_success = [200]

    def _should_retry(self, status_code: int) -> bool:
        return True if status_code in self.status_codes_to_retry else False

    def _is_response_code_valid(self, status_code: int) -> bool:
        return True if status_code in self.status_codes_success else False

    def get_data(self, source: APISource, application_id: str, realm: REALM, account_id: str = None, token: str = None,
                 nickname: str = None):
        """
        Generic method to extract data for an endpoint and validate the result
        """
        request_factory = RequestFactory(
            application_id=application_id,
            account_id=account_id,
            realm=realm,
            token=token,
            source=source
        )

        prepped_request = request_factory.prepare_request(nickname=nickname)
        data = self._make_request(prepped_request)
        return data.json()

    def _make_request(self, request) -> requests.Response:
        """
        Requests data with the retry functionality
        """
        logging.info(f"Request URL: {request.url}")
        attempt = 0

        while attempt <= self.MAX_ATTEMPTS:
            attempt += 1
            session = Session()
            response = session.send(request)

            if self._should_retry(response.status_code) and attempt <= self.MAX_ATTEMPTS:
                waiting_seconds = attempt * self.BACKOFF_MULTIPLIER
                logging.warning(f"Status code {response.status_code}: sleeping for {waiting_seconds} seconds")
                time.sleep(waiting_seconds)

            elif self._is_response_code_valid(response.status_code):
                return response

            else:
                response.raise_for_status()

