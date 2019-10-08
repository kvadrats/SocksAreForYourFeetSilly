from core.objects import logger


def _join(*args):
    return "\n".join(map(lambda x: str(x), filter(lambda x: x is not None, args)))


class AbstractException(Exception):
    def __init__(self, message):
        logger.exception(message)
        super(AbstractException, self).__init__(message)


class NoWebServiceCredentialsProvided(AbstractException):
    def __init__(self):
        message = "No credentials mapped from Environment to webservice system component"
        super(NoWebServiceCredentialsProvided, self).__init__(message)


class AbstractTechnicalComponent(AbstractException):
    def __init__(self, message=None, prefix=None, suffix=None):
        message = _join(
            prefix,
            message,
            suffix
        )
        super(AbstractTechnicalComponent, self).__init__(message)


class JsonWebServiceException(AbstractTechnicalComponent):
    def __init__(self, exception):
        message = _join(
            'JSON WebService Server raised fault or exception during response getting.',
            str(exception),
            exception.__class__.__name__,
            exception.message
        )
        super(JsonWebServiceException, self).__init__(message)
