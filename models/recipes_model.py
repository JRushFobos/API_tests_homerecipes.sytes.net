import random

from faker import Faker

from models.base_model import BaseModel
from test_utils.utils_func import (create_random_image_base64,
                                   generate_HEX_color_code,
                                   get_random_ingredients_with_amount,
                                   get_random_tags)

faker = Faker()


class RecipesModel(BaseModel):
    def __init__(self):
        self.ingredients = get_random_ingredients_with_amount()
        self.tags = get_random_tags()
        self.image = create_random_image_base64("png")
        self.name = faker.name()
        self.text = generate_HEX_color_code()
        self.cooking_time = random.randint(5, 60)
