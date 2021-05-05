from gensim.models import KeyedVectors
import time

PATH = './vec/model.vec'

if __name__ == '__main__':
    start = time.time()
    for i in range(0, 11):
        wv = KeyedVectors.load_word2vec_format(PATH, binary=False)
        del wv
    elapsed_time = time.time() - start
    print("time: {0}".format(elapsed_time) + " [sec]")
