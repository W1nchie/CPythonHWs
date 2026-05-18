import os
import multiprocessing
def worker(q):
    message = q.get()
    print(f"PID {os.getpid()} получил сообщение: {message}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    queue.put("Привет из главного процесса")
    p.join()