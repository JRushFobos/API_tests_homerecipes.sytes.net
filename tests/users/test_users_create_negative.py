import allure
from faker import Faker

from models.users_model import UsersModel
from supported_classes.http_client import CustomHttpClient as client

faker = Faker()


@allure.suite("TestUsersNegative")
class TestCreateUsersNegative:
    @allure.title("Test create user without email status code")
    def test_create_users_without_email_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["email"]
        with allure.step("Get response without email"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user without username status code")
    def test_create_users_without_username_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["username"]
        with allure.step("Get response without username"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user without password status code")
    def test_create_users_without_password_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["password"]
        with allure.step("Get response without password"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user without first name status code")
    def test_create_users_without_first_name_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["first_name"]
        with allure.step("Get response without first_name"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user without email status code")
    def test_create_users_without_last_name_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        del data["last_name"]
        with allure.step("Get response without last_name"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user email with boolean status_code")
    def test_create_users_email_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["email"] = faker.boolean()
        with allure.step("Get response email with boolean"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user email with text status code")
    def test_create_users_email_with_text_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["email"] = faker.lexify(text=f"{'?' * 12}")
        with allure.step("Get response email with text"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user email with letters status code")
    def test_create_users_email_with_letters_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["email"] = faker.lexify(letters="!@#$^&*()_+")
        with allure.step("Get response email with letters"):
            response = (client().disable_authorization()
                        .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user password with boolean status code")
    def test_create_users_password_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["password"] = faker.boolean()
        with allure.step("Get response password with boolean"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user first_name with boolean status code")
    def test_create_users_first_name_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["first_name"] = faker.boolean()
        with allure.step("Get response first_name with boolean"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"

    @allure.title("Test create user last_name with boolean status code")
    def test_create_users_last_name_with_boolean_status_code(self):
        user = UsersModel()
        data = user.to_dict()
        data["last_name"] = faker.boolean()
        with allure.step("Get response last_name with boolean"):
            response = (client().disable_authorization()
                                .post("/api/users/", data=data))
        with allure.step("Check assert status code"):
            assert (
                response.status_code == 400
            ), f"Status not 400, current status: {response.status_code}"
