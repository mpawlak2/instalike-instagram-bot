import time

class Bot:
    __algorithms = []

    def __init__(self):
        pass

    def run(self):
        for algorithm in self.__algorithms:
            algorithm.run()
            time.sleep(1 / 60)