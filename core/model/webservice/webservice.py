import pprint

from core.common.config import Config
from core.common.exceptions import NoWebServiceCredentialsProvided, JsonWebServiceException
from core.libs.request_lib import send_post_json, send_get_json
from core.objects import logger


class JsonWebServiceComponent:
    def __init__(self, area=None):
        if not hasattr(self, "credentials"):
            raise NoWebServiceCredentialsProvided()

        if area:
            timeout = Config[f"{area}"]["timeout"]
        else:
            timeout = Config["default"]["timeout"]

        _definition = {
            "endpoint": None,
            "login": None,
            "password": None,
            "timeout": timeout
        }

        for key, value in _definition.items():
            if self.credentials.get(key):
                value = self.credentials.get(key)
            _definition[key] = value

        self._config = self.credentials = _definition.copy()

    def send_post_request(self, payload):
        # payload['credentials']['username'] = self._config['login']
        # payload['credentials']['password'] = self._config['password']
        logger.info("Send JSON thru POST to url {}".format(self._config['endpoint']))
        logger.info("Sending payload: \n{}".format(pprint.pformat(payload)))
        try:
            response = send_post_json(self._config['endpoint'], payload)
            logger.info("POST response: \n{}".format(pprint.pformat(response)))
        except Exception as e:
            raise JsonWebServiceException(e)
        return response

    def send_get_request(self, payload=None, url_ending=None):
        # payload['credentials']['username'] = self._config['login']
        # payload['credentials']['password'] = self._config['password']
        endpoint = self._config['endpoint'] + "/" + url_ending if url_ending else self._config['endpoint']
        logger.info("Send JSON thru POST to url {}".format(endpoint))
        logger.info("Sending payload: \n{}".format(pprint.pformat(payload)))
        try:
            response = send_get_json(endpoint, payload)
            logger.info("GET response: \n{}".format(pprint.pformat(response)))
        except Exception as e:
            raise JsonWebServiceException(e)
        return response
