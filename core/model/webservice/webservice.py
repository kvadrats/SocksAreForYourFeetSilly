from core.common.exceptions import NoWebServiceCredentialsProvided


class JsonWebServiceComponent:
    def __init__(self):
        if not hasattr(self, "credentials"):
            raise NoWebServiceCredentialsProvided(
                "No credentials mapped from Environment to webservice system component"
            )

        _definition = {
            "endpoint": None,
            "login": None,
            "password": None,
            "timeout": Config["timeout.webservice"]
        }

        # todo: refactor - self.credentials will be defined in nested classes as property to Class object
        for key, value in _definition.iteritems():
            if self.credentials.get(key):
                value = self.credentials.get(key)
            _definition[key] = value

        self._config = self.credentials = _definition.copy()

    def send_request(self, payload):
        payload['credentials']['username'] = self._config['login']
        payload['credentials']['password'] = self._config['password']
        logging.info("Send JSON thru POST to url {}".format(self._config['endpoint']))
        logging.info("Sending payload: \n{}".format(pprint.pformat(payload)))
        try:
            response = send_post_json(self._config['endpoint'], payload)
            logging.info("Get response: \n{}".format(pprint.pformat(response)))
        except Exception as e:
            raise JsonWebServiceException(e)
        return response
