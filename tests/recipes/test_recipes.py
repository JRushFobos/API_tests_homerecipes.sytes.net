from jsonschema import validate

from schemas.recipes_schema import (valid_schema_recipes,
                                    valid_schema_recipes_array)
from supported_classes.http_client import CustomHttpClient as client
from models.recipes_model import RecipesModel

class TestRecipes:
    def test_create_recipes_status_code_schema(self):
        user = RecipesModel()
        data = user.to_dict()
        response = client().post("/api/recipes/", data=data)
        assert (
            response.status_code == 201
        ), f"Status not 201, current status: {response.status_code}"
        assert (
            validate(response.json(), schema=valid_schema_recipes) is None
        ), "Response body not validate"

    def test_get_recipes_list_status_code_schema(self):
        response = client().get("/api/recipes/")
        assert (
            response.status_code == 200
        ), f"Status not 200, current status: {response.status_code}"
        assert (
            validate(response.json(), schema=valid_schema_recipes_array) is None
        ), "Response body not validate"

    def test_get_recipes_details_status_code_schema(self, get_recipe_id):
        response = client().get(f"/api/recipes/{get_recipe_id}/")
        assert (
            response.status_code == 200
        ), f"Status not 200, current status: {response.status_code}"
        assert (
            validate(response.json(), schema=valid_schema_recipes) is None
        ), "Response body not validate"


    def test_delete_recipe_status_code_schema(self):
        user = RecipesModel()
        data = user.to_dict()
        response_create = client().post("/api/recipes/", data=data)
        recipe_id = response_create.json()["id"]
        response_delete = client().delete(f"/api/recipes/{recipe_id}/")
        assert (
            response_delete.status_code == 204
        ), f"Status not 200, current status: {response_delete.status_code}"

    def test_patch_recipe_status_code_schema(
            self, get_recipe_id):
        user = RecipesModel()
        data = user.to_dict()
        response = client().patch(f"/api/recipes/{get_recipe_id}/", data=data)
        assert (
            response.status_code == 200
        ), f"Status not 200, current status: {response.status_code}"
