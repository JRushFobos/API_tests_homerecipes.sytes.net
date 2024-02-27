import random
import allure
from faker import Faker

from models.recipes_model import RecipesModel
from supported_classes.http_client import CustomHttpClient as client

faker = Faker()


@allure.feature("TestRecipesNegativePatch")
class TestRecipesNegativePatch:
    @allure.title("test_patch_recipes_without_token")
    def test_patch_recipes_without_token_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        with allure.step("Get response"):
            response = (
                client()
                .disable_authorization()
                .patch(f"/api/recipes/{get_recipe_id}/", data=data)
            )
        with allure.step("Check assert"):
            assert (
            response.status_code == 401
        ), f"Status not 401, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_letter_ingredients_id")
    def test_patch_recipes_with_letter_ingredients_id_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_ingredients_id")
    def test_patch_recipes_with_boolean_ingredients_id_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_letter")
    def test_patch_recipes_with_letter_ingredients_amount_status_code(
        self, get_recipe_id
    ):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean")
    def test_patch_recipes_with_boolean_ingredients_amount_status_code(
        self, get_recipe_id
    ):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_letter_tags")
    def test_patch_recipes_with_letter_tags_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_tags")
    def test_patch_recipes_with_boolean_tags_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_letter_image")
    def test_patch_recipes_with_letter_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_image")
    def test_patch_recipes_with_boolean_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_int_image")
    def test_patch_recipes_with_int_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = random.randint(1, 1000)
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_letter_name")
    def test_patch_recipes_with_letter_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_name")
    def test_patch_recipes_with_boolean_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_int_name")
    def test_patch_recipes_with_int_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = random.randint(1, 1000)
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_text")
    def test_patch_recipes_with_boolean_text_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["text"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_cooking_time")
    def test_patch_recipes_with_boolean_cooking_time_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_int_cooking_time")
    def test_patch_recipes_with_int_cooking_time_status_code(self,
                                                             get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                       data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_boolean_cooking_time")
    def test_patch_recipes_with_boolean_cooking_time_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("test_patch_recipes_with_int_cooking_time")
    def test_patch_recipes_with_int_cooking_time_status_code(self,
                                                             get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"
