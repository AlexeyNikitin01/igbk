import logging

from PIL import Image
from igbk.settings import BASE_DIR
from kandinsky2 import get_kandinsky2


def generate_image(prompt: str, realize: bool = False) -> Image:
    if realize:
        model = get_kandinsky2("cuda")
        images = model.generate_text2img(
            prompt=prompt,
            num_steps=100,
            batch_size=1,
            guidance_scale=4,
            h=768, w=768,
            sampler='p_sampler',
            prior_cf_scale=4,
            prior_steps="5"
        )
        image = images[0]
        return image
    logging.info("BASE IMAGE IN GENERATE IMAGE")
    image = Image.open(BASE_DIR / "main\\static\\grusha.jpg", mode='r')
    return image


if __name__ == "__main__":
    prompt = "черный кот в HD качестве"
    generate_image(prompt, realize=False)
