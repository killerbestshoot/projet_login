from time import *

import Aunthentification as aut
import dispatch

if __name__ == '__main__':
    for i in range(200):
        e = "-" * i
    print(e)
    sleep(1)
    aut.auth()
