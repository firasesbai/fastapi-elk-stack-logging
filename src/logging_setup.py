import logging

# Central log format for root logger
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"


def setup_root_logger():
    """ Setup configuration of the root logger of the application """

    # get instance of root logger
    logger = logging.getLogger('')

    # configure formatter for logger
    formatter = logging.Formatter(LOG_FORMAT)

    # configure console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    # configure rotating file handler
    file = logging.handlers.RotatingFileHandler(filename="logs/fastapi-elk-stack.log", mode='a',
                                                maxBytes=15000000, backupCount=5)
    file.setFormatter(formatter)

    # add handlers
    logger.addHandler(console)
    logger.addHandler(file)

    # configure logger level
    logger.setLevel(logging.INFO)
