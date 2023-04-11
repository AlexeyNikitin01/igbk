from .image_generation import fake_gen
from .keyword_generation import prompt_to_generate


def gen_img(keywords: list):
    p = prompt_to_generate(keywords)
    # img_url = generate_image(prompt=p)
    img_url = fake_gen(prompt=p)
    return img_url


if __name__ == "__main__":
    print("main.py return ->", gen_img([40, 'black skin']))
