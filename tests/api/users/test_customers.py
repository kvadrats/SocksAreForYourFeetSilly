from tests.api.users.common import UserTestCase

from tests.api.common import APITestCase, AbstractJsonWS
from core.common.config import Config


class CustomerJsonWS(AbstractJsonWS):
    credentials = Config["customers"]


class TestCustomers(UserTestCase):
    json = CustomerJsonWS()
    def test_customers(self):
        result = self.json.send_get_request()
        print(result)
