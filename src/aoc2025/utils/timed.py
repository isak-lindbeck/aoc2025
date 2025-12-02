import time


class Timed:

    def __enter__(self):
        self.start = time.time()


    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start
        print()
        print(f"Duration: {int(duration * 1000)} ms")