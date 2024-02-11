import os
import pytest
import json

from supported_classes.http_client import CustomHttpClient as client


# @pytest.fixture(scope='class')
def get_token():
    body = {"email": os.getenv('LOGIN'),
            "password": os.getenv('PASSWORD')}
    request = (client().disable_authorization()
               .post("/api/auth/token/login/", data=body))
    return request.json()["auth_token"]
