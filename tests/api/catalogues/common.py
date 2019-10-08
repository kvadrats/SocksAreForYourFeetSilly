from tests.api.common import APITestCase, AbstractJsonWS
from core.common.config import Config

import core.model.webservice.requests as req


class CataloguesJsonWS(AbstractJsonWS):
    credentials = Config["catalogues"]


class CataloguesTestCase(APITestCase):
    json = CataloguesJsonWS()
    requests = req
