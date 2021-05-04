from infrastructure.models import Bookmark, BookmarkSchema
from service.nlp import obtain_word_embeddings, get_text_by_ogp
from infrastructure.milvus import save_vector


def save_bookmark(bm_request):
    bm = Bookmark()
    bm.url = bm_request['url']
    bm.memo = bm_request['memo']
    bm.ogp = bm_request['ogp']
    ogp_sentenct = get_text_by_ogp(bm.ogp)
    if ogp_sentenct != '':
        vector = obtain_word_embeddings('{} {}'.format(bm.memo, ogp_sentenct))
    else:
        vector = obtain_word_embeddings(bm.memo)

    bm = bm.save(bm)

    return save_vector('bookmarks', vector, bm.id)
