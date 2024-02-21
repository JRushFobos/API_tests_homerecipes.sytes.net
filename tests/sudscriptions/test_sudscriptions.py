from jsonschema import validate

from supported_classes.http_client import CustomHttpClient as client
from schemas.subscriptions_schema import (valid_schema_tags,
                                          valid_schema_sudscriptions_array)

class TestSubscriptions:
    def test_get_list_subscriptions_status_code_id_schema(self,
                                                          get_new_user_id):
        client().post(f"/api/users/{get_new_user_id}/subscribe/")
        response = client().get("/api/users/subscriptions/")
        client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        assert (response.status_code == 200
                ), f"Status not 200, current status: {response.status_code}"
        assert(response.json()["results"][0]["id"] == get_new_user_id
               ), "Invalid user has been subscribed"
        assert validate(
             response.json()["results"], schema=valid_schema_sudscriptions_array
            ) is None, "Response body not validate"

    def test_post_subscribe_status_code_id_schema(self, get_new_user_id):
        response = client().post(f"/api/users/{get_new_user_id}/subscribe/")
        client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        assert (response.status_code == 201
                ), f"Status not 201, current status: {response.status_code}"
        assert(response.json()["id"] == get_new_user_id
               ), "Invalid user has been subscribed"
        assert validate(
             response.json(), schema=valid_schema_tags
            ) is None, "Response body not validate"

    def test_delete_subscribe_status_code_schema(self, get_new_user_id):
        client().post(f"/api/users/{get_new_user_id}/subscribe/")
        response = client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        assert (response.status_code == 204
                ), f"Status not 204, current status: {response.status_code}"
        repeat_response = (client()
                           .delete(f"/api/users/{get_new_user_id}/subscribe/"))
        assert (repeat_response.status_code == 400
                ), ("Repeat delete status not 400,"
                     f"current status: {repeat_response.status_code}")
