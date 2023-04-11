import unittest


from keyword_generation import prompt_to_generate
from image_generation import fake_gen


class TestCaseGenerateImage(unittest.TestCase):

    def test_keyword(self):
        prompt = '40 black skin'
        self.assertEqual(prompt, prompt_to_generate([40, 'black skin']))

    # def test_generate(self):
    #     url = "..\\main\\static\\output\\albert.jpg"
    #     prompt = '40 black skin'
    #     self.assertEqual(url, fake_gen(prompt=prompt))


