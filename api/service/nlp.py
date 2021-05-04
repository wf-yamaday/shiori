from service.janome import get_wakati
from service.vector import get_vector


def obtain_word_embeddings(text):
    word_list = get_wakati(text)
    return get_vector(word_list)


def get_text_by_ogp(ogp):
    text_info = ''
    if 'og:title' in ogp:
        text_info += ' {}'.format(ogp['og:title'])
    if 'og:description' in ogp:
        text_info += ' {}'.format(ogp['og:description'])
    return text_info
