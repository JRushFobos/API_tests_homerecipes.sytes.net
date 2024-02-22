from jsonschema import validate

from schemas.tags_schema import valid_schema_tags, valid_schema_tags_array
from supported_classes.http_client import CustomHttpClient as client


class TestTags:
    def test_get_tags_arrey_status_code_schema(self):
        response = client().disable_authorization().get("/api/tags/")
        assert (
            response.status_code == 200
        ), f"Status not 200, current status: {response.status_code}"
        assert (
            validate(response.json(), schema=valid_schema_tags_array) is None
        ), "Response body not validate"

    def test_get_tags_detail_status_code_schema(self, get_random_tag_id):
        response = (
            client().disable_authorization().get(f"/api/tags/{get_random_tag_id}")
        )
        assert (
            response.status_code == 200
        ), f"Status not 200, current status: {response.status_code}"
        assert (
            validate(response.json(), schema=valid_schema_tags) is None
        ), "Response body not validate"
