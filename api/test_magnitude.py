from pymagnitude import Magnitude
import time

PATH = './vec/model.magnitude'

if __name__ == '__main__':
    start = time.time()
    for i in range(0, 11):
        wv = Magnitude(PATH)
        del wv
    elapsed_time = time.time() - start
    print("time:{0} ".format(elapsed_time) + " [sec]")
