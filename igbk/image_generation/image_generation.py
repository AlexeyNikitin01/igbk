import random
from PIL import Image
from pathlib import Path
# from kandinsky2 import get_kandinsky2
#
#
# def generate_image(prompt: str):
#     model = get_kandinsky2("cuda")
#     images = model.generate_text2img(
#         prompt=prompt,
#         num_steps=100,
#         batch_size=1,
#         guidance_scale=4,
#         h=768, w=768,
#         sampler='p_sampler',
#         prior_cf_scale=4,
#         prior_steps="5"
#     )
#     output = Path("../main/static/output")
#     output.mkdir(parents=True, exist_ok=True)
#     u = output / f"{random.randint(10, 100)}.png"
#     images[0].save(u)
#     return str(u)


def fake_gen(prompt: str = None):
    output = Path("../main/static/output")
    output.mkdir(parents=True, exist_ok=True)
    print("create done", output / "albert.jpg")
    img = Image.open(Path("../main/static") / "albert.jpg")
    img.save(output / "albert.jpg")
    return str(output / "albert.jpg")


if __name__ == "__main__":
    prompt = "черный кот в HD качестве"
    fake_gen(prompt)
