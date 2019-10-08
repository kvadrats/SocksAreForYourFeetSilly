from tests.api.common import APITestCase, AbstractJsonWS
from core.common.config import Config

import core.model.webservice.requests as req


class UserJsonWS(AbstractJsonWS):
    credentials = Config["users"]


class UserTestCase(APITestCase):
    json = UserJsonWS()
    requests = req
