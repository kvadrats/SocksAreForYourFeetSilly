from tests.api.users.common import UserTestCase


class TestUserRegistration(UserTestCase):
    def test_user_registration(self):
        payload = self.requests.REGISTRATION_FORM
        payload["username"] = "timmy"
        payload["password"] = "yourmom"
        payload["email"] = "emial@emal.lv"
        result = self.user.send_post_request(payload)
        print(result)
