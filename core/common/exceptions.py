from core.objects import logger


class AbstractException(Exception):
    def __init__(self, message):
        logger.exception(message)
        super(AbstractException, self).__init__(message)


class NoWebServiceCredentialsProvided(AbstractException):
    def __init__(self):
        message = "No credentials mapped from Environment to webservice system component"
        super(NoWebServiceCredentialsProvided, self).__init__(message)
