from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
import time
import sys
import math

def standard_integrate(f, a, b, *, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def task(f, a, b, n_iter, task_name):
    print("task {} start".format(task_name))
    res = standard_integrate(f, a, b, n_iter=n_iter)
    print("task {} finish".format(task_name))
    return res

def integrate(f, a, b, *, Pool, n_jobs, n_iter=10000000):
    with Pool(n_jobs) as executor:
        # разбиваем задачу на n_jobs задач
        step = (b - a) / n_jobs
        futures = [executor.submit(task, f, a + i * step, a + (i + 1) * step, n_iter // n_jobs, i) for i in range(n_jobs)]

    return reduce(lambda x,y: x + y, [future.result() for future in futures])

if __name__ == '__main__':
    args = [math.cos, 0, math.pi / 2]

    # assert(abs(standard_integrate(*args) - integrate(*args)) < 1e-6)

    for n_jobs in range(1, 21):
        for Pool in [ThreadPoolExecutor, ProcessPoolExecutor]:
            print("-------------n_jobs={}---Pool={}-------------".format(n_jobs, Pool))
            begin = time.time()
            integrate(*args, Pool=Pool, n_jobs=n_jobs)
            delta = time.time() - begin
            print("time: {} s".format(delta))



