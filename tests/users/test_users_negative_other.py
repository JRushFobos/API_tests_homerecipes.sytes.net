import random
import string

from faker import Faker

from models.users_model import UsersModel
from supported_classes.http_client import CustomHttpClient as client
from test_utils.utils_func import generate_fake_token

faker = Faker()


class TestUsers:
    def test_get_current_users_without_token_status(self):
        response = client().disable_authorization().get("/api/users/me/")
        assert (
            response.status_code == 401
        ), f"Status not 401 current status: {response.status_code}"

    def test_get_users_detail_with_incorrect_id_status_code(self):
        id = random.randint(10000, 50000)
        response = client().get(f"/api/users/{id}/")
        assert (
            response.status_code == 404
        ), f"Status not 200 OK, current status: {response.status_code}"

    def test_post_change_users_password_status_check_login(self, get_data_for_login):
        new_password = faker.password()
        body = {
            "new_password": new_password,
            "current_password": get_data_for_login["password"],
        }
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json;charset=utf-8",
            "Authorization": f"Token {get_data_for_login['token']}",
        }
        response = (
            client()
            .set_headers(headers)
            .disable_authorization()
            .post(f"/api/users/set_password/", data=body)
        )
        assert (
            response.status_code == 401
        ), f"Status not 401, current status: {response.status_code}"

    def test_post_users_login_with_incorrect_creds_status_code(self):
        user = UsersModel()
        del user.first_name, user.last_name, user.username
        response = client().post(f"/api/auth/token/login/", data=user.to_dict())
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_post_users_login_with_incorrect_password_status_code(
        self, get_data_for_login
    ):
        user = UsersModel()
        del user.first_name, user.last_name, user.username
        user.email = get_data_for_login["email"]
        response = client().post(f"/api/auth/token/login/", data=user.to_dict())
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_post_delete_users_token_with_incorrect_token_status_code(self):
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json;charset=utf-8",
            "Authorization": f"Token {generate_fake_token()}",
        }
        response = client().set_headers(headers).post(f"/api/auth/token/logout/")
        assert (
            response.status_code == 401
        ), f"Status not 401, current status: {response.status_code}"
