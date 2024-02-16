from jsonschema import validate

from supported_classes.http_client import CustomHttpClient as client
from schemas.ingridients_schema import (valid_schema_ingridients,
                                        valid_schema_ingridients_array)


class TestInredients():
    def test_get_inredients_arrey_status_code_schema(self):
        response = (client().disable_authorization()
                            .get("/api/ingredients/"))
        assert (response.status_code == 200
                ), f"Status not 200, current status: {response.status_code}"
        assert validate(
             response.json(), schema=valid_schema_ingridients_array
            ) is None, "Response body not validate"

    def test_get_inredients_detail_status_code_schema(
            self, get_random_inredient_id):
        response = (client().disable_authorization()
                            .get(f"/api/ingredients//{get_random_inredient_id}"))
        assert (response.status_code == 200
                ), f"Status not 200, current status: {response.status_code}"
        assert validate(
             response.json(), schema=valid_schema_ingridients
            ) is None, "Response body not validate"
