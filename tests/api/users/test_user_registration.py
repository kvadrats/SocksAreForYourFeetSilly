from tests.api.users.common import UserTestCase


class TestUserRegistration(UserTestCase):
    def test_user_registration(self):
        payload = self.requests.USER_POST_REGISTER
        payload["id"] = "123555"
        result = self.json.send_request(payload)
        print(result)
