import pytest
import random
from faker import Faker

from supported_classes.http_client import CustomHttpClient as client
from models.recipes_model import RecipesModel

faker = Faker()

class TestRecipesNegativePatch:
    def test_patch_recipes_without_token_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        response = (client().disable_authorization()
                           .patch(f"/api/recipes/{get_recipe_id}/", data=data))
        assert (
            response.status_code == 401
        ), f"Status not 401, current status: {response.status_code}"

    def test_patch_recipes_with_letter_ingredients_id_status_code(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_ingredients_id_status_code(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["id"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_letter_ingredients_amount_status_code(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_ingredients_amount_status_code(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["ingredients"][0]["amount"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_letter_tags_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_tags_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["tags"][0] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_letter_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_int_image_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["image"] = random.randint(1, 1000)
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"


    def test_patch_recipes_with_letter_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_int_name_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["name"] = random.randint(1, 1000)
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_text_status_code(self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["text"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_boolean_cooking_time_status_code(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_int_cooking_time_status_code(
            self, get_recipe_id ):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"


    def test_patch_recipes_with_boolean_cooking_time_status_code(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.boolean()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"

    def test_patch_recipes_with_int_cooking_time_status_code(
            self, get_recipe_id ):
        user = RecipesModel()
        data = user.to_dict()
        data["cooking_time"] = faker.lexify(letters="!@#$^&*()_+")
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 400
        ), f"Status not 400, current status: {response.status_code}"
