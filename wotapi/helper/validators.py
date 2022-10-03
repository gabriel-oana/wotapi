import logging


class Validators:

    @staticmethod
    def check_if_param_exists(param: str, param_type: str):
        """
        Checks if the token / account_id / application id has been provided.
        """

        if param:
            if param_type:
                return True
            else:
                logging.error('Parameter Type {} has not been provided'.format(param_type))
                raise ValueError('Parameter Type {} has not been provided'.format(param_type))

        else:
            logging.error('Parameter {} has not been provided'.format(param))
            raise ValueError('Parameter {} has not been provided'.format(param))

    @staticmethod
    def check_realm(realm: str):
        """
        Checks if the realm selected is correct.
        """

        if realm in ['eu', 'ru', 'na', 'asia']:
            return True
        else:
            logging.error('Realm {} incorrect. Please choose from: eu, ru, na or asia'.format(realm))
            raise ValueError('Realm {} incorrect. Please choose from: eu, ru, na or asia'.format(realm))
