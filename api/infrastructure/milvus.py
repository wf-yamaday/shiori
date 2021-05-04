import requests
import json

MILVUS_HOST = 'http://127.0.0.1:19121'


def init_milvus(name):
    param = {'collection_name': name, 'dimension': 300,
             'index_file_size': 1024, 'metric_type': 'IP'}
    r = requests.post(
        '{}/collections'.format(MILVUS_HOST), data=json.dumps(param)
    )
    if r.status_code != 201:
        print('[error]', r.text)
        return False
    return True


def save_vector(name, vector, id):
    param = {'vectors': [vector.tolist()], 'ids': [str(id)]}
    r = requests.post(
        '{}/collections/{}/vectors'.format(MILVUS_HOST, name),
        data=json.dumps(param)
    )
    if r.status_code != 201:
        print('[error]', r.text)
        return False
    return True


def get_vector_by_id(name, id):
    r = requests.get(
        '{}/collections/{}/vectors?ids={}'.format(MILVUS_HOST, name, id)
    )
    if r.status_code != 200:
        print('[error]', r.text)
    return r.json()


def search(name, vector):
    param = {
        'search': {
            'topk': 10,
            'vectors': [vector],
            'params': {
                'nprobe': 16,
            }
        }
    }
    r = requests.put(
        '{}/collections/{}/vectors'.format(MILVUS_HOST, name),
        data=json.dumps(param)
    )
    if r.status_code != 200:
        print('[error]', r.text)
    return r.json()
