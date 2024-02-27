import allure
from jsonschema import validate

from schemas.tags_schema import valid_schema_tags, valid_schema_tags_array
from supported_classes.http_client import CustomHttpClient as client


@allure.suite("TestTags")
class TestTags:
    @allure.title("Test get tags list status code, schema")
    def test_get_tags_arrey_status_code_schema(self):
        with allure.step("Get response list tags"):
            response = client().disable_authorization().get("/api/tags/")
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check validate schema"):
            assert (
                validate(response.json(),
                         schema=valid_schema_tags_array) is None
            ), "Response body not validate"

    @allure.title("Test get tag detail status code, schema")
    def test_get_tags_detail_status_code_schema(self, get_random_tag_id):
        with allure.step("Get response tag detail"):
            response = (client().disable_authorization()
                                .get(f"/api/tags/{get_random_tag_id}"))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 200
            ), f"Status not 200, current status: {response.status_code}"
        with allure.step("Check validate schema"):
            assert (
                validate(response.json(), schema=valid_schema_tags) is None
            ), "Response body not validate"
