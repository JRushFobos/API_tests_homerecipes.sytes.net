from jsonschema import validate

from supported_classes.http_client import CustomHttpClient as client
from models.users_model import UsersModel
from schemas.users_schema import valid_schema_users, valid_schema_users_array


class TestUsers:
    def test_create_user_status_code_schema(self):
        user = UsersModel()
        data = user.to_dict()
        response = client().disable_authorization().post("/api/users/",
                                            data=data)
        assert((response.status_code == 201),
                f"Status not 4xx, current status: {response.status_code}")
        assert(validate(response.json(), schema=valid_schema_users) is None,
                "Response body not validate")

    def test_get_user_list_status_code_schema(self):
        response = client().disable_authorization().get("/api/users/")
        assert((response.status_code == 200),
               f"Status not 4xx, current status: {response.status_code}")
        assert validate(response.json()["results"], schema=valid_schema_users_array) is None

    # def test_get_user_detail_status_code_schema(self):
    #     response = client().disable_authorization().get("/api/users/")
    #     assert((response.status_code == 200),
    #            f"Status not 4xx, current status: {response.status_code}")
    #     assert(validate(response.json(), schema=valid_schema_users) is None,
    #             "Response body not validate")
