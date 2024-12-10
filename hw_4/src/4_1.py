from threading import Thread
from multiprocessing import Process
import time

def fib(n: int):
    if n == 0:
        return 0
    
    prev1 = 0
    res = 1
    for _ in range(1, n):
        prev2 = prev1
        prev1 = res
        res = prev1 + prev2

    return res

class Task:
    def __init__(self, work, kwargs):
        self.work = work
        self.kwargs = kwargs

    def run(self):
        self.work(**self.kwargs)
    

class ThreadChecker(Thread):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks

    def run(self):
        for cur in self.tasks:
            cur.run()

class ProcessChecker(Process):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = tasks

    def run(self):
        for cur in self.tasks:
            cur.run()
        

if __name__ == '__main__':
    with open("artifacts/4_1.txt", 'w') as file:
        task = Task(fib, {'n': 100000})

        t = ThreadChecker([task for _ in range(10)])
        begin = time.time()
        t.start()
        t.join()
        delta = time.time() - begin
        file.write("1 поток, 10 задач:\n")  
        file.write(str(delta) + " s\n")

        p = ProcessChecker([task for _ in range(10)])
        begin = time.time()
        p.start()
        p.join()
        delta = time.time() - begin
        file.write("1 процесс, 10 задач:\n")  
        file.write(str(delta) + " s\n")

        file.write("-------------------------\n")

        threads = [ThreadChecker([task]) for _ in range(10)]
        begin = time.time()
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        delta = time.time() - begin
        file.write("10 потоков, 1 задача:\n")  
        file.write(str(delta) + " s\n")

        processes = [ProcessChecker([task]) for _ in range(10)]
        begin = time.time()
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        delta = time.time() - begin
        file.write("10 процессов, 1 задача:\n")  
        file.write(str(delta) + " s\n")
    