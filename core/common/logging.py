import datetime
import logging

standard_logging = logging


class AbstractLogger(object):
    pass


class Logger(AbstractLogger):

    def __init__(self):
        self._build_filename()

        logger = standard_logging.getLogger(self.logname)
        logger.setLevel(standard_logging.DEBUG)

        fh = standard_logging.FileHandler(self.logname, mode='a', delay=False,
                                          encoding="utf-8")
        fh.setLevel(standard_logging.DEBUG)

        sh = standard_logging.StreamHandler()
        sh.setLevel(standard_logging.CRITICAL)

        formatter = standard_logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)
        self.logger = logger

    def _build_filename(self):
        timestamp = str(datetime.datetime.now()).replace(" ", "_").split(".")[0].replace(":", "-")
        self.logname = f'logs/{timestamp}.txt'

    def print_and_log(self, data):
        self.logger.debug(data)
        print(data)
