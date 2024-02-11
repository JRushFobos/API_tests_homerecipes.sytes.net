from faker import Faker

from models.base_model import BaseModel

faker = Faker()


class UsersModel(BaseModel):
    def __init__(self):
        self.email = faker.email()
        self.username = faker.user_name()
        self.password = faker.password()
        self.first_name = faker.first_name()
        self.last_name = faker.last_name()
