valid_schema_recipes = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "color": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"},
                    "slug": {"type": "string"}
                },
            }
        },
        "author": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "email": {"type": "string", "format": "email"},
                "is_subscribed": {"type": "boolean"}
            },
        },
        "ingredients": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "measurement_unit": {"type": "string"},
                    "amount": {"type": "integer"}
                },
            }
        },
        "is_favorited": {"type": "boolean"},
        "is_in_shopping_cart": {"type": "boolean"},
        "image": {"type": "string", "format": "uri"},
        "name": {"type": "string"},
        "text": {"type": "string"},
        "cooking_time": {"type": "integer"}
    },
}

valid_schema_recipes_array = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "color": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"},
                    "slug": {"type": "string"},
                },
            },
        },
        "author": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "username": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "email": {"type": "string", "format": "email"},
                "is_subscribed": {"type": "boolean"},
            },
        },
        "ingredients": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "measurement_unit": {"type": "string"},
                    "amount": {"type": "integer"},
                },
            },
        },
        "is_favorited": {"type": "boolean"},
        "is_in_shopping_cart": {"type": "boolean"},
        "image": {"type": "string", "format": "uri"},
        "name": {"type": "string"},
        "text": {"type": "string"},
        "cooking_time": {"type": "integer"},
    },
}
