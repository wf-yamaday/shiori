import numpy as np
from pymagnitude import Magnitude

PATH = './vec/model.magnitude'

vectors = Magnitude(PATH)


def get_vector(word_list):
    vec = vectors.query(word_list)
    return np.sum(vec, axis=0)
