valid_schema_users = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "minLength": 1, "maxLength": 254},
        "username": {"type": "string", "minLength": 1, "maxLength": 150},
        "password": {"type": "string", "minLength": 1, "maxLength": 150},
        "first_name": {"type": "string", "minLength": 1, "maxLength": 150},
        "last_name": {"type": "string", "minLength": 1, "maxLength": 150},
    }
}

valid_schema_users_array = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "minLength": 1, "maxLength": 254},
            "username": {"type": "string", "minLength": 1, "maxLength": 150},
            "password": {"type": "string", "minLength": 1, "maxLength": 150},
            "first_name": {"type": "string", "minLength": 1, "maxLength": 150},
            "last_name": {"type": "string", "minLength": 1, "maxLength": 150},
        }
    },
}
