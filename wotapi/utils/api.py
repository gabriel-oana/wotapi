import logging
import time
from requests import Session
from wotapi.utils.request_factory import RequestFactory


class API:

    def __init__(self, application_id: str, realm: str, account_id: str = None, token: str = None):
        self.account_id = account_id
        self.application_id = application_id
        self.access_token = token
        self.realm = realm
        self.MAX_ATTEMPTS = 3
        self.BACKOFF_MULTIPLIER = 10

    def get_data(self, source: str, nickname: str = None):
        """
        Generic method to extract data for an endpoint and validate the result
        """
        request_factory = RequestFactory(
            application_id=self.application_id,
            account_id=self.account_id,
            realm=self.realm,
            token=self.access_token,
            source=source
        )

        prepped_request = request_factory.prepare_request(nickname=nickname)

        attempt = 0
        while attempt <= self.MAX_ATTEMPTS:
            attempt += 1
            session = Session()
            r = session.send(prepped_request)

            if self._eval_response(r, attempt):
                return r.json()
            else:
                continue

    def _eval_response(self, response, attempt: int) -> bool:
        """
        Evaluates the status code of the get request
        """

        if response.status_code == 200:
            # TODO: This needs a better implementation
            # Check the response for the correct responses.

            try:
                message = response.json()['error']['message']
                code = response.json()['error']['code']
            except:
                logging.info('API call success: Status Code 200')
                message = None
                code = None

            if message and code:
                logging.error("HTTP Response Code: {} - Message: {}".format(code, message))
                raise ConnectionError("HTTP Response Code: {} - Message: {}".format(code, message))
            else:
                return True

        if response.status_code != 200:
            waiting_seconds = attempt * self.BACKOFF_MULTIPLIER
            logging.warning("HTTP Error Code: {} - Attempt: {} - Will retry again in {}"
                            .format(response.status_code, attempt, attempt * self.BACKOFF_MULTIPLIER))
            time.sleep(waiting_seconds)
