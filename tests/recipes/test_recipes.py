import allure

from jsonschema import validate

from models.recipes_model import RecipesModel
from schemas.recipes_schema import (valid_schema_get_recipes,
                                    valid_schema_post_recipes,
                                    valid_schema_recipes_array)
from supported_classes.http_client import CustomHttpClient as client
from test_utils.utils_func import compare_recipes_values


@allure.feature("TestRecipes")
class TestRecipes:
    @allure.title("test_create_recipes_without_token_status_code")
    def test_create_recipes_status_code_schema(self):
        user = RecipesModel()
        data = user.to_dict()
        with allure.step("Create recipe"):
            response = client().post("/api/recipes/", data=data)
        id = response.json()["id"]
        with allure.step("Delete recipe"):
            client().delete(f"/api/recipes/{id}/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 201
            ), f"Status not 201, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json(),
                         schema=valid_schema_post_recipes) is None
            ), "Response body not validate"

    @allure.title("test_get_recipes_list_status_code_schema")
    def test_get_recipes_list_status_code_schema(self):
        with allure.step("Get response"):
            response = client().get("/api/recipes/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json(),
                         schema=valid_schema_recipes_array) is None
            ), "Response body not validate"

    @allure.title("test_get_recipes_details_status_code_schema")
    def test_get_recipes_details_status_code_schema(self, get_recipe_id):
        with allure.step("Get response"):
            response = client().get(f"/api/recipes/{get_recipe_id}/")
        with allure.step("Check assert status_code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check assert validate schema"):
            assert (
                validate(response.json(),
                         schema=valid_schema_get_recipes) is None
            ), "Response body not validate"

    @allure.title("test_delete_recipe_status_code_schema")
    def test_delete_recipe_status_code_schema(self):
        user = RecipesModel()
        data = user.to_dict()
        with allure.step("Create recipe"):
            response_create = client().post("/api/recipes/", data=data)
        recipe_id = response_create.json()["id"]
        with allure.step("Delete recipe"):
            response_delete = client().delete(f"/api/recipes/{recipe_id}/")
        with allure.step("Assert delete recipe"):
            assert (
                response_delete.status_code == 204
            ), f"Status not 200, current status: {response_delete.status_code}"

    @allure.title("test_patch_recipe_status_code_compare_values")
    def test_patch_recipe_status_code_compare_values(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        with allure.step("Check patch recipe"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check patch recipe data"):
            assert (
                compare_recipes_values(data, response.json()) is True
            ), "Created fields data not the same data in file"
