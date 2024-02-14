from jsonschema import validate
from faker import Faker

from supported_classes.http_client import CustomHttpClient as client
from models.users_model import UsersModel

faker = Faker()

class TestUsersNegative:
    def test_create_user_without_email_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["email"]
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_without_username_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["username"]
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_without_password_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["password"]
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_without_first_name_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["first_name"]
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_without_last_name_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["last_name"]
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_email_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["email"] = faker.boolean()
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_email_with_text_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["email"] = faker.lexify(text=f"{'?' * 12}")
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_email_with_text_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["email"] = faker.lexify(letters='!@#$^&*()_+')
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_password_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["password"] = faker.boolean()
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_first_name_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["first_name"] = faker.boolean()
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    def test_create_user_last_name_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["last_name"] = faker.boolean()
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"
