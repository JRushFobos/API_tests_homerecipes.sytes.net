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
@allure.title("Fixture get_data_for_login token/password/email")
def get_data_for_login():
    change_password_data = {}
    user = UsersModel()
    data = user.to_dict()
    with allure.step("create user"):
        client().disable_authorization().post("/api/users/", data=data)
    user_data = {"email": user.email, "password": user.password}
    with allure.step("request to get token"):
        request = (
            client().disable_authorization().post("/api/auth/token/login/", data=user_data)
        )
    with allure.step("Get token/password/email"):
        change_password_data["token"] = request.json()["auth_token"]
        change_password_data["password"] = user.password
        change_password_data["email"] = user.email
    return change_password_data


@pytest.fixture(scope="class")
@allure.title("Fixture get_new_user_id")
def get_new_user_id():
    user = UsersModel()
    with allure.step("Get response"):
        response = (client().disable_authorization()
                            .post("/api/users/", data=user.to_dict()))
    return response.json()["id"]


@pytest.fixture(scope="class")
@allure.title("Fixture get_recipe_id")
def get_random_tag_id():
    with allure.step("Get response"):
        response = client().disable_authorization().get("/api/tags/")
    with allure.step("Get random tag id"):
        tag_id = random.choices(range(1, len(response.json())))
    return tag_id[0]


@pytest.fixture(scope="class")
@allure.title("Fixture get random inredient id")
def get_random_inredient_id():
    with allure.step("Get inredients"):
        response = client().disable_authorization().get("/api/ingredients/")
    with allure.step("Random choices inredient"):
        inredient_id = random.choices(range(1, len(response.json())))
    return inredient_id[0]


@pytest.fixture(scope="class")
@allure.title("Fixture get_recipe_id")
def get_recipe_id():
    user = RecipesModel()
    data = user.to_dict()
    with allure.step("Create recipes"):
        response = client().post("/api/recipes/", data=data)
    with allure.step("Get recipe id"):
        recipe_id = response.json()["id"]
    yield recipe_id
    with allure.step("Fixture delete recipe id"):
        client().delete(f"/api/recipes/{recipe_id}/")
