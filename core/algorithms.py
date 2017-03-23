from abc import ABC, abstractmethod


class Algorithm(ABC):
    @abstractmethod
    def run(self):
        pass


class LikeAlgorithm(Algorithm):
    __operations = None

    def __init__(self, operations):
        self.__operations = operations

    def run(self):
        pass
