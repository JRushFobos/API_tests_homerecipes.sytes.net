import os
import random

import pytest
import allure

from models.recipes_model import RecipesModel
from models.users_model import UsersModel
from supported_classes.http_client import CustomHttpClient as client


@pytest.fixture(scope="class")
def get_token():
    body = {"email": os.getenv("LOGIN"), "password": os.getenv("PASSWORD")}
    request = client().disable_authorization().post("/api/auth/token/login/", data=body)
    return request.json()["auth_token"]


@pytest.fixture(scope="class")
def get_data_for_login():
    change_password_data = {}
    user = UsersModel()
    data = user.to_dict()
    client().disable_authorization().post("/api/users/", data=data)
    user_data = {"email": user.email, "password": user.password}
    request = (
        client().disable_authorization().post("/api/auth/token/login/", data=user_data)
    )
    change_password_data["token"] = request.json()["auth_token"]
    change_password_data["password"] = user.password
    change_password_data["email"] = user.email
    return change_password_data


@pytest.fixture(scope="class")
def get_new_user_id():
    user = UsersModel()
    response = client().disable_authorization().post("/api/users/", data=user.to_dict())
    return response.json()["id"]


@pytest.fixture(scope="class")
def get_random_tag_id():
    response = client().disable_authorization().get("/api/tags/")
    tag_id = random.choices(range(1, len(response.json())))
    return tag_id[0]


@pytest.fixture(scope="class")
def get_random_inredient_id():
    response = client().disable_authorization().get("/api/ingredients/")
    inredient_id = random.choices(range(1, len(response.json())))
    return inredient_id[0]


@pytest.fixture(scope="class")
@allure.title("Fixture get_recipe_id")
def get_recipe_id():
    user = RecipesModel()
    data = user.to_dict()
    response = client().post("/api/recipes/", data=data)
    with allure.step("Fixture get recipe id"):
        recipe_id = response.json()["id"]
    yield recipe_id
    with allure.step("Fixture delete recipe id"):
        client().delete(f"/api/recipes/{recipe_id}/")
