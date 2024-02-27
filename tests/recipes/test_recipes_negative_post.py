import random
import allure

import pytest
from faker import Faker

from models.recipes_model import RecipesModel
from supported_classes.http_client import CustomHttpClient as client

faker = Faker()


@allure.feature("TestRecipesNegativePost")
class TestRecipesNegativePost:
    @pytest.mark.skip(reason="error 500 ISE")
    @allure.title("test_create_recipes_without_token_status_code")
    def test_create_recipes_without_token_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        with allure.step("Get response"):
            response = client().disable_authorization().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 401
        ), f"Status not 401, current status: {response.status_code}"

    def test_create_recipes_with_letter_ingredients_id_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_ingredients_id_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_letter_ingredients_amount_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_ingredients_amount_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_letter_tags_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_tags_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_letter_image_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_image_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_int_image_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = random.randint(1, 1000)
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_letter_name_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_name_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_int_name_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = random.randint(1, 1000)
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_text_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["text"] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_boolean_cooking_time_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_create_recipes_with_int_cooking_time_status_code(self):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response"):
            response = client().post("/api/recipes/", data=data)
        with allure.step("Check assert"):
            assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"
