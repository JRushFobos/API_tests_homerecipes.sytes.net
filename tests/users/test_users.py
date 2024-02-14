from jsonschema import validate
from faker import Faker

from supported_classes.http_client import CustomHttpClient as client
from models.users_model import UsersModel
from schemas.users_schema import valid_schema_users, valid_schema_users_array

faker = Faker()

class TestUsers:
    def test_create_user_status_code_schema(self):
        user = UsersModel()
        data = user.to_dict()
        response = client().disable_authorization().post("/api/users/",
                                                         data=data)
        assert(
             response.status_code == 201
            ), f"Status not 201, current status: {response.status_code}"
        assert validate(
             response.json(), schema=valid_schema_users
            ) is None, "Response body not validate"

    def test_get_user_list_status_code_schema(self):
        response = client().disable_authorization().get("/api/users/")
        assert (
             response.status_code == 200
            ), f"Status not 200 OK, current status: {response.status_code}"
        assert validate(
            response.json()["results"], schema=valid_schema_users_array
            ) is None

    def test_get_current_user_status_code_schema(self):
        response = client().get("/api/users/me/")
        assert (response.status_code == 200
               ), f"Status not 200 OK, current status: {response.status_code}"
        assert validate(response.json(), schema=valid_schema_users
              ) is None, "Response body not validate"

    def test_get_user_detail_status_code_schema(self, get_new_user_id):
        id = get_new_user_id
        response = client().get(f"/api/users/{id}/")
        assert (response.status_code == 200
               ), f"Status not 200 OK, current status: {response.status_code}"
        assert validate(response.json(), schema=valid_schema_users
              ) is None, "Response body not validate"

    def test_post_change_user_password_status_check_login(
            self, get_data_for_login):
        new_password = faker.password()
        body = {
            "new_password": new_password,
            "current_password": get_data_for_login["password"]
        }
        headers =  {
            "Content-Type": "application/json",
            "accept": "application/json;charset=utf-8",
            "Authorization": f"Token {get_data_for_login['token']}"
        }
        response = (client().set_headers(headers)
                           .post(f"/api/users/set_password/", data=body))
        assert (response.status_code == 204
               ), f"Status not 204, current status: {response.status_code}"
        login_body = {"email": get_data_for_login["email"],
                     "password": new_password}
        login_check_response = (client()
                               .set_headers(headers)
                               .post(f"/api/auth/token/login/",
                                     data=login_body))
        assert (login_check_response.status_code == 200
               ), f"Status not 200, current status: {response.status_code}"

    def test_post_delete_token_status(
            self, get_data_for_login):
        headers =  {
            "Content-Type": "application/json",
            "accept": "application/json;charset=utf-8",
            "Authorization": f"Token {get_data_for_login['token']}"
        }
        response = (client().set_headers(headers)
                            .post(f"/api/auth/token/logout/"))
        assert (response.status_code == 204
               ), f"Status not 204, current status: {response.status_code}"
        response = (client().set_headers(headers)
                            .post(f"/api/auth/token/logout/"))
        assert (response.status_code == 401
               ), f"Status not 401, current status: {response.status_code}"
