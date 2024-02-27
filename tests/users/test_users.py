import allure
from faker import Faker
from jsonschema import validate

from models.users_model import UsersModel
from schemas.users_schema import valid_schema_users, valid_schema_users_array
from supported_classes.http_client import CustomHttpClient as client

faker = Faker()

@allure.suite("TestUsersPositive")
class TestUsers:
    @allure.title("Test create user check status code, schema")
    def test_create_users_status_code_schema(self):
        user = UsersModel()
        data = user.to_dict()
        with allure.step("Create users"):
            response = (client().disable_authorization()
                               .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 201
            ), f"Status not 201, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json(), schema=valid_schema_users) is None
            ), "Response body not validate"

    @allure.title("Test get users list check status code, schema")
    def test_get_users_list_status_code_schema(self):
        with allure.step("Get list users"):
            response = client().disable_authorization().get("/api/users/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 200
            ), f"Status not 200 OK, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json()["results"],
                         schema=valid_schema_users_array)is None)

    @allure.title("Test get current user status  code, schema")
    def test_get_current_users_status_code_schema(self):
        with allure.step("Get current user"):
            response = client().get("/api/users/me/")
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 200
            ), f"Status not 200 OK, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json(), schema=valid_schema_users) is None
            ), "Response body not validate"

    @allure.title("Test get user detail status code, schema")
    def test_get_users_detail_status_code_schema(self, get_new_user_id):
        with allure.step("Get users detail"):
            response = client().get(f"/api/users/{get_new_user_id}/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 200
            ), f"Status not 200 OK, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json(), schema=valid_schema_users) is None
            ), "Response body not validate"

    @allure.title("Test post change user password status code, check login")
    def test_post_change_users_password_status_check_login(self,
                                                           get_data_for_login):
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
        with allure.step("Change user password"):
            response = (
                client().set_headers(headers)
                        .post(f"/api/users/set_password/", data=body)
            )
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 204
            ), f"Status not 204, current status: {response.status_code}"
        login_body = {"email": get_data_for_login["email"],
                      "password": new_password}
        with allure.step("Login with new password"):
            login_check_response = (
                client()
                .set_headers(headers)
                .post(f"/api/auth/token/login/", data=login_body)
            )
        with allure.step("Check assert status_code"):
            assert (
                login_check_response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"

    @allure.title("Test post delete token (logout) status code")
    def test_post_delete_token_status(self, get_data_for_login):
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json;charset=utf-8",
            "Authorization": f"Token {get_data_for_login['token']}",
        }
        with allure.step("Logout"):
            response = (client().set_headers(headers)
                                .post(f"/api/auth/token/logout/"))
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 204
            ), f"Status not 204, current status: {response.status_code}"
        with allure.step("Logout one more time"):
            response = (client().set_headers(headers)
                               .post(f"/api/auth/token/logout/"))
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 401
            ), f"Status not 401, current status: {response.status_code}"
