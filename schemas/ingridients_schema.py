valid_schema_ingridients = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "minLength": 1, "maxLength": 200},
        "color": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"},
        "slug": {"type": "string", "minLength": 1, "maxLength": 200},
    },
}

valid_schema_ingridients_array = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string", "minLength": 1, "maxLength": 200},
            "color": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"},
            "slug": {"type": "string", "minLength": 1, "maxLength": 200},
        },
    },
}
