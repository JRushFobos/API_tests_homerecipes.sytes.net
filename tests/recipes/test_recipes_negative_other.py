import random
import allure

from faker import Faker

from supported_classes.http_client import CustomHttpClient as client

faker = Faker()

@allure.suite("TestRecipesNegative")
class TestRecipesOther:
    @allure.title("Test get recipes incorrect id randint")
    def test_get_recipes_details_incorrect_id_status_code(self):
        with allure.step("Get response"):
            response = client().get(f"/api/recipes/{random.randint(10000,20000)}/")
        with allure.step("Check assert"):
            assert response.status_code == 404, (
                "Status not 404, " f"current status: {response.status_code}"
            )

    @allure.title("Test delete recipes incorrect id randint")
    def test_delete_recipes_incorrect_id_status_code(self):
        with allure.step("Get response"):
            response = client().delete(f"/api/recipes/{random.randint(10000,20000)}/")
        with allure.step("Check assert"):
            assert response.status_code == 404, (
                "Status not 404, " f"current status: {response.status_code}"
            )

    @allure.title("Test delete recipes without token")
    def test_delete_recipes_without_token_status_code(self, get_recipe_id):
        response = (
            client().disable_authorization().delete(f"/api/recipes/{get_recipe_id}/")
        )
        assert response.status_code == 401, (
            "Status not 401, " f"current status: {response.status_code}"
        )
