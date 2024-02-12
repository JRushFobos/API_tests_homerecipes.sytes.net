import os
import pytest
import json

from supported_classes.http_client import CustomHttpClient as client
from models.users_model import UsersModel

@pytest.fixture(scope='class')
def get_token():
    body = {"email": os.getenv('LOGIN'),
            "password": os.getenv('PASSWORD')}
    request = (client().disable_authorization()
               .post("/api/auth/token/login/", data=body))
    return request.json()["auth_token"]

@pytest.fixture(scope="class")
def get_data_for_change_password():
    change_password_data = {}
    user = UsersModel()
    data = user.to_dict()
    client().disable_authorization().post("/api/users/", data=data)
    user_data = {"email": user.email, "password": user.password}
    request = client().disable_authorization().post("/api/auth/token/login/", data=user_data)
    change_password_data["token"] = request.json()["auth_token"]
    change_password_data["password"] = user.password
    return change_password_data

@pytest.fixture(scope="class")
def get_new_user_id():
    user = UsersModel()
    data = user.to_dict()
    response = client().disable_authorization().post("/api/users/",
                                        data=data)
    print(response.text)
    print(response.content)
    response_json = json.loads(response.text)
    return response_json["id"]
