import os
import multiprocessing


def square(x):
    return x * x


def increment(shared_val, lock):
    for _ in range(1000):
        with lock:
            shared_val.value += 1


def worker_receiver(conn):
    number = conn.recv()
    conn.send(number ** 2)
    conn.close()


def register_process(shared_dict):
    name = multiprocessing.current_process().name
    pid = os.getpid()
    shared_dict[name] = pid