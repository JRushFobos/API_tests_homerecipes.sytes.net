import allure
from jsonschema import validate

from schemas.subscriptions_schema import (valid_schema_sudscriptions_array,
                                          valid_schema_tags)
from supported_classes.http_client import CustomHttpClient as client


@allure.suite("TestSubscriptionsPositive")
class TestSubscriptions:
    @allure.title("Test get list subscriptions status code, schema")
    def test_get_list_subscriptions_status_code_schema(self,
                                                          get_new_user_id):
        with allure.step("Create subscribe"):
            client().post(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Get list subscribers"):
            response = client().get("/api/users/subscriptions/")
        with allure.step("Delete subscriber"):
            client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json()["results"],
                         schema=valid_schema_sudscriptions_array)
                         is None
            ), "Response body not validate"

    @allure.title("Test post subscribe status code, check id, schema")
    def test_post_subscribe_status_code_id_schema(self, get_new_user_id):
        with allure.step("Create subscribe"):
            response = client().post(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Delete subscribe"):
            client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 201
            ), f"Status not 201, current status: {response.status_code}"
        with allure.step("Check subscribe id"):
            assert (
                response.json()["id"] == get_new_user_id
            ), "Invalid user has been subscribed"
        with allure.step("Check validate schema"):
            assert (
                validate(response.json(), schema=valid_schema_tags) is None
            ), "Response body not validate"

    @allure.title("Test unsubscribe status code, double unsubscribe")
    def test_delete_subscribe_status_code_schema(self, get_new_user_id):
        with allure.step("Create subscribe"):
            client().post(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Delete subscribe"):
            response = (client().delete(
                        f"/api/users/{get_new_user_id}/subscribe/"))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 204
            ), f"Status not 204, current status: {response.status_code}"
        with allure.step("Delete subscribe one more time "):
            repeat_response = (client().delete(
                               f"/api/users/{get_new_user_id}/subscribe/"))
        with allure.step("Delete subscribe one more time status_code"):
            assert repeat_response.status_code == 400, (
                "Repeat delete status not 400,"
                f"current status: {repeat_response.status_code}"
            )
