from faker import Faker

from models.base_model import BaseModel
from test_utils.utils_func import generate_HEX_color_code

faker = Faker()


class TagsModel(BaseModel):
    def __init__(self):
        self.name = faker.name()
        self.color = generate_HEX_color_code()
        self.slug = faker.text()
