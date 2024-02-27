import allure

from jsonschema import validate

from schemas.ingridients_schema import (valid_schema_ingridients,
                                        valid_schema_ingridients_array)
from supported_classes.http_client import CustomHttpClient as client


@allure.suite("TestInredients")
class TestInredients:
    @allure.title("Test get inredients list status code, schema")
    def test_get_inredients_arrey_status_code_schema(self):
        with allure.step("Get inredients list"):
            response = client().disable_authorization().get("/api/ingredients/")
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check validate schema"):
            assert (
                validate(response.json(),
                         schema=valid_schema_ingridients_array) is None
            ), "Response body not validate"

    @allure.title("Test get inredient detail status code, schema")
    def test_get_inredients_detail_status_code_schema(self,
                                                      get_random_inredient_id):
        with allure.step("Get inredients detail"):
            response = (
                client()
                .disable_authorization()
                .get(f"/api/ingredients/{get_random_inredient_id}")
            )
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check validate schema"):
            assert (
                validate(response.json(),
                         schema=valid_schema_ingridients) is None
            ), "Response body not validate"
