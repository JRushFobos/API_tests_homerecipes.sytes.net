valid_schema_tags = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "image": {"type": "string"},
        "cooking_time": {"type": "integer"},
    }
}


valid_schema_sudscriptions_array = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "email": {"type": "string"},
            "username": {"type": "string"},
            "first_name": {"type": "string"},
            "last_name": {"type": "string"},
            "is_subscribed": {"type": "boolean"},
            "recipes": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "image": {"type": "string"},
                        "cooking_time": {"type": "integer"},
                    },
                },},
            "recipes_count": {"type": "integer"},
        }
    },
}
