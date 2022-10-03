import logging


def create_logger(log_level: str):
    """
    Creates a logger object
    """
    logging.basicConfig(level=log_level,
                        filename='app.log', filemode='a+',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger("WorldOfTanksAPI")

    return logger
