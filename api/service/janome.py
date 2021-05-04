from janome.tokenizer import Tokenizer

t = Tokenizer()


def get_wakati(text):
    return list(t.tokenize(text, wakati=True))
