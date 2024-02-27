import random
import allure
from faker import Faker

from models.recipes_model import RecipesModel
from supported_classes.http_client import CustomHttpClient as client

faker = Faker()


@allure.suite("TestRecipesNegative")
class TestRecipesNegativePatch:
    @allure.title("Test patch recipes without token")
    def test_patch_recipes_without_token_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        with allure.step("Get response"):
            response = (
                client()
                .disable_authorization()
                .patch(f"/api/recipes/{get_recipe_id}/", data=data)
            )
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 401
        ), f"Status not 401, current status: {response.status_code}"

    @allure.title("Test patch recipes with letter ingredients id")
    def test_patch_recipes_with_letter_ingredients_id_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean ingredients id")
    def test_patch_recipes_with_boolean_ingredients_id_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with letters ingredients amount status")
    def test_patch_recipes_with_letter_ingredients_amount_status_code(
        self, get_recipe_id
    ):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean status code")
    def test_patch_recipes_with_boolean_ingredients_amount_status_code(
        self, get_recipe_id
    ):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with letters tags status code")
    def test_patch_recipes_with_letter_tags_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean tags status code")
    def test_patch_recipes_with_boolean_tags_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with letters image status code")
    def test_patch_recipes_with_letter_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean image status code")
    def test_patch_recipes_with_boolean_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with randint image status code")
    def test_patch_recipes_with_int_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = random.randint(1, 1000)
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with letter name status code")
    def test_patch_recipes_with_letter_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean name status code")
    def test_patch_recipes_with_boolean_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with randint name status code")
    def test_patch_recipes_with_int_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = random.randint(1, 1000)
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean text status code")
    def test_patch_recipes_with_boolean_text_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["text"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean cooking time status code")
    def test_patch_recipes_with_boolean_cooking_time_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with letters cooking_time status code")
    def test_patch_recipes_with_letters_cooking_time_status_code(self,
                                                             get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                       data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with boolean cooking_time status code")
    def test_patch_recipes_with_boolean_cooking_time_status_code(
        self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test patch recipes with letters cooking_time status code")
    def test_patch_recipes_with_letters_cooking_time_status_code(self,
                                                             get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().patch(f"/api/recipes/{get_recipe_id}/",
                                      data=data)
        with allure.step("Check assert status code"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"
