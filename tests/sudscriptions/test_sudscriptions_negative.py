import pytest
import random
from faker import Faker

from supported_classes.http_client import CustomHttpClient as client

faker = Faker()

class TestSubscriptions:
    @pytest.mark.skip(reason="status code 500 ISE")
    def test_get_list_subscriptions_without_token_status_code(self,
                                                          get_new_user_id):
        client().post(f"/api/users/{get_new_user_id}/subscribe/")
        response = (client().disable_authorization()
                           .get("/api/users/subscriptions/"))
        client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        assert (response.status_code == 401
                ), f"Status not 401, current status: {response.status_code}"


    def test_post_subscribe_without_token_status_code(self, get_new_user_id):
        response = (client().disable_authorization()
                           .post(f"/api/users/{get_new_user_id}/subscribe/"))
        client().delete(f"/api/users/{get_new_user_id}/subscribe/")
        assert (response.status_code == 400
                ), f"Status not 400, current status: {response.status_code}"


    def test_delete_subscribe_without_token_status_code(self, get_new_user_id):
        client().post(f"/api/users/{get_new_user_id}/subscribe/")
        response = (client().disable_authorization()
                           .delete(f"/api/users/{get_new_user_id}/subscribe/"))
        assert (response.status_code == 400
                ), f"Status not 400, current status: {response.status_code}"


    def test_post_subscribe_on_incorrect_user_status_code(self):
        id = random.randint(10000,50000)
        response = (client().post(f"/api/users/{id}/subscribe/"))
        assert (response.status_code == 404
                ), f"Status not 404, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    def test_post_subscribe_on_incorrect_user_letters_status_code(self):
        id = faker.lexify(letters='!@#$^&*()_+')
        response = (client().post(f"/api/users/{id}/subscribe/"))
        assert (response.status_code == 400
                ), f"Status not 400, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    def test_post_subscribe_on_incorrect_user_boolean_status_code(self):
        id = faker.boolean()
        response = (client().post(f"/api/users/{id}/subscribe/"))
        assert (response.status_code == 400
                ), f"Status not 400, current status: {response.status_code}"

    def test_delete_subscribe_on_incorrect_user_status_code(self):
        id = random.randint(10000,50000)
        response = (client().delete(f"/api/users/{id}/subscribe/"))
        assert (response.status_code == 404
                ), f"Status not 404, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    def test_delete_subscribe_on_incorrect_user_letters_status_code(self):
        id = faker.lexify(letters='!@#$^&*()_+')
        response = (client().delete(f"/api/users/{id}/subscribe/"))
        assert (response.status_code == 400
                ), f"Status not 400, current status: {response.status_code}"

    @pytest.mark.skip(reason="status code 500 ISE")
    def test_delete_subscribe_on_incorrect_user_boolean_status_code(self):
        id = faker.boolean()
        response = (client().delete(f"/api/users/{id}/subscribe/"))
        assert (response.status_code == 400
                ), f"Status not 400, current status: {response.status_code}"
