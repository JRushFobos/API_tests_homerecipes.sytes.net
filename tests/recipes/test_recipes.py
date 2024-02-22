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
        print(data)
        assert (
            response.status_code == 201
        ), f"Status not 201, current status: {response.status_code}"
        assert (
            validate(response.json(), schema=valid_schema_recipes) is None
        ), "Response body not validate"
