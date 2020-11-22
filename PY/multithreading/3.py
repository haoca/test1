import threading
import time
from queue import Queue


def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)  # 任务间隔0.1s
    print("T1 finish\n")


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        # t.start()
        threads.append(t)
        print(t)
    for thread in threads:
        thread.start()
        thread.join()
    results = []
    for i in range(4):
        results.append(q.get())
    print(results)


if __name__ == "__main__":

    multithreading()
# added_thread = threading.Thread(target=thread_job, name='T1')
# added_thread.start()
# print("all done\n")

# for i in range(10):
#     time.sleep(3)
# print('s')
