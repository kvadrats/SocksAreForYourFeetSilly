from tests.common import TestCase
from core.common.config import Config
from core.model.webservice.webservice import JsonWebServiceComponent


class AbstractJsonWS(JsonWebServiceComponent):
    credentials = {}


class APITestCase(TestCase):
    json = AbstractJsonWS()
