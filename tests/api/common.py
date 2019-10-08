from core.common.config import Config
from core.model.webservice.webservice import JsonWebServiceComponent
from tests.common import TestCase
import core.model.webservice.requests as req


class CustomerJsonWS(JsonWebServiceComponent):
    credentials = Config["customers"]


class UserJsonWS(JsonWebServiceComponent):
    credentials = Config["users"]


class CataloguesJsonWS(JsonWebServiceComponent):
    credentials = Config["catalogues"]


class APITestCase(TestCase):
    requests = req
    customer = CustomerJsonWS()
    user = UserJsonWS()
    catalogue = CataloguesJsonWS()
