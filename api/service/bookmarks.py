from infrastructure.models import Bookmark, BookmarkSchema
from service.nlp import obtain_word_embeddings, get_text_by_ogp
from infrastructure.milvus import save_vector, get_vector_by_id, search


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


def get_bookmark_by_id(id):
    bookmark = Bookmark().find_one(id)
    res = get_vector_by_id('bookmarks', id)
    res = search('bookmarks', res['vectors'][0]['vector'])
    result = filter(lambda i: int(i['id']) >
                    0 and int(i['id']) != id, res['result'][0])
    ids = [i.get('id') for i in list(result)]
    related_bookmarks = Bookmark().find_by_ids(list(ids))
    return BookmarkSchema().dump(bookmark), BookmarkSchema(many=True).dump(related_bookmarks)
