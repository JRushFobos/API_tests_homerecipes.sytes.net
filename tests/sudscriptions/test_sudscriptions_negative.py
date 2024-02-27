import random
import allure

import pytest
from faker import Faker

from supported_classes.http_client import CustomHttpClient as client

faker = Faker()


@allure.suite("TestSubscriptionsNegative")
class TestSubscriptionsNegative:
    @pytest.mark.skip(reason="status code 500 ISE")
    @allure.title("Test get list subscriptions without token status code")
    def test_get_list_subscriptions_without_token_status_code(self,
                                                              get_new_user_id):
        with allure.step("Create subscribe"):
            client().post(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Get list subscribers"):
            response = (client().disable_authorization()
                                .get("/api/users/subscriptions/"))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 401
            ), f"Status not 401, current status: {response.status_code}"

    @allure.title("Test post subscribe without token status code")
    def test_post_subscribe_without_token_status_code(self, get_new_user_id):
        with allure.step("Create subscribe without_token"):
            response = (
                client()
                .disable_authorization()
                .post(f"/api/users/{get_new_user_id}/subscribe/")
            )
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test unsubscribe without token status code")
    def test_delete_subscribe_without_token_status_code(self, get_new_user_id):
        with allure.step("Create subscribe"):
            client().post(f"/api/users/{get_new_user_id}/subscribe/")
        with allure.step("Delete subscribe without_token"):
            response = (
                client()
                .disable_authorization()
                .delete(f"/api/users/{get_new_user_id}/subscribe/")
            )
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test post subscribe on incorrect user status code")
    def test_post_subscribe_on_incorrect_user_status_code(self):
        id = random.randint(10000, 50000)
        with allure.step("Subscribe on incorrect_user"):
            response = client().post(f"/api/users/{id}/subscribe/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 404
            ), f"Status not 404, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    @allure.title("Test post subscribe on incorrect user(letters) status_code")
    def test_post_subscribe_on_incorrect_user_letters_status_code(self):
        id = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Subscribe on incorrect user id letters"):
            response = client().post(f"/api/users/{id}/subscribe/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    @allure.title("Test post subscribe on incorrect user boolean status code")
    def test_post_subscribe_on_incorrect_user_boolean_status_code(self):
        id = faker.boolean()
        with allure.step("Subscribe on incorrect user id boolean"):
            response = client().post(f"/api/users/{id}/subscribe/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test unsubscribe on incorrect user status code")
    def test_delete_subscribe_on_incorrect_user_status_code(self):
        id = random.randint(10000, 50000)
        with allure.step("delete subscribe on incorrect user id randint"):
            response = client().delete(f"/api/users/{id}/subscribe/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 404
            ), f"Status not 404, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    @allure.title("Test unsubscribe on incorrect user letters status code")
    def test_delete_subscribe_on_incorrect_user_letters_status_code(self):
        id = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("delete subscribe on incorrect user id letters"):
            response = client().delete(f"/api/users/{id}/subscribe/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    @allure.title("Test unsubscribe on incorrect user boolean status code")
    def test_delete_subscribe_on_incorrect_user_boolean_status_code(self):
        id = faker.boolean()
        with allure.step("delete subscribe on incorrect user id boolean"):
            response = client().delete(f"/api/users/{id}/subscribe/")
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"
