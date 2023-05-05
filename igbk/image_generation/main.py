from PIL import Image

from .image_generation import generate_image
from .keyword_generation import prompt_to_generate


def gen_img(keywords: list, realize: bool =False) -> Image:
    p = prompt_to_generate(keywords)
    img = generate_image(prompt=p, realize=realize)
    return img


if __name__ == "__main__":
    print("main.py return ->", gen_img([40, 'black skin']))
