import base64
import io
import random
import string

from faker import Faker
from PIL import Image

from supported_classes.http_client import CustomHttpClient as client


def generate_HEX_color_code():
    color_code = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color_code


def generate_fake_token():
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(40)
    )


def get_random_ingredients_with_amount():
    ingredient = {}
    ingredients = []
    response = client().disable_authorization().get("/api/ingredients/")
    random_ingredient = random.choice(response.json())
    ingredient["id"] = random_ingredient["id"]
    ingredient["amount"] = random.randint(1, 1000)
    ingredients.append(ingredient)
    return ingredients


def get_random_tags():
    tags = []
    response = client().disable_authorization().get("/api/tags/")
    tag_id = random.choices(range(1, len(response.json())))
    tags.append(tag_id[0])
    return tags


def create_random_image_base64(
    format_file: str, width: int = None, height: int = None
) -> str:
    faker = Faker()
    width = width or faker.random_int(min=100, max=600)
    height = height or faker.random_int(min=100, max=600)
    image = Image.new("RGB", (width, height))
    image_io = io.BytesIO()
    image.save(image_io, format=format_file)
    image_io.seek(0)
    image_base64 = base64.b64encode(image_io.getvalue()).decode("utf-8")
    return f"data:image/{format_file};base64,{image_base64}"
