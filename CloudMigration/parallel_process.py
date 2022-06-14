from multiprocessing import Process
from time import sleep
from datetime import datetime

Pros = []


def function_x(i):
    sleep(3)
    print(i)
    print(datetime.now())


def function_y():
    print("done")


def main():
    for i in range(0, 3):
        print("Thread Started")
        p = Process(target=function_x, args=(i,))
        Pros.append(p)
        p.start()

    # block until all the threads finish (i.e. block until all function_x calls finish)
    for t in Pros:
        t.join()

    function_y()


main()