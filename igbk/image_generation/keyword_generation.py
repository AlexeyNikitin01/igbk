

def prompt_to_generate(keywords: list):
    keywords = list(map(str, keywords))
    print("create keywords")
    return ' '.join(keywords)


if __name__ == "__main__":
    kw = [40, 'black skin']
    print(prompt_to_generate(kw), type(prompt_to_generate(kw)))
