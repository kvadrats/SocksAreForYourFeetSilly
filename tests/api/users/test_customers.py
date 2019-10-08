from tests.api.users.common import UserTestCase


class TestCustomers(UserTestCase):

    def test_customers(self):
        result = self.customer.send_get_request()
        print(result)
