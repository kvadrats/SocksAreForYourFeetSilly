from tests.api.users.common import UserTestCase


class TestUserRegistration(UserTestCase):
    def test_user_registration(self):
        payload = self.requests.REGISTRATION_FORM
        payload["username"] = "test"
        payload["password"] = "test2"
        payload["email"] = "em@email.lv"
        result = self.user.send_post_request(payload)
        reg_id = result['id']

    def test_registration_success(self):
        result = self.USER_GET_CUSTOMERID.send_get_request()
        print(result)
