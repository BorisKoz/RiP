import time
from contextlib import contextmanager


class cm_timer_1:

    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, traceback):
        end_time = time.time()
        if exc_type is not None:
            print(exc_type, exc_val, traceback)
        else:
            print('time: ', end_time - self.start)


@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    end = time.time()
    print('time: ', end - start)


def main():
    with cm_timer_1():
        time.sleep(2.5)

    with cm_timer_2():
        time.sleep(2.5)
if __name__ == '__main__':
    main()

