valid_schema_tags = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "minLength": 1, "maxLength": 200},
        "measurement_unit": {"type": "string", "minLength": 1, "maxLength": 200},
    }
}

valid_schema_tags_array = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string", "minLength": 1, "maxLength": 200},
            "measurement_unit": {"type": "string", "minLength": 1, "maxLength": 200},
        }
    },
}
