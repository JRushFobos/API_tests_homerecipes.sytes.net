import random
import string



def generate_HEX_color_code():
    color_code = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color_code


def generate_fake_token():
    return "".join(random.choice(string.ascii_letters + string.digits)
                              for _ in range(40))
