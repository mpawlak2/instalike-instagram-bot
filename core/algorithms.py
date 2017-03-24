from abc import ABC, abstractmethod


class Algorithm(ABC):
    __operations = None

    def __init__(self, operations):
        self.__operations = operations

    @abstractmethod
    def run(self):
        pass


class LikeAlgorithm(Algorithm):
    def __init__(self):
        pass

    def run(self):
        pass


class FollowAlgorithm(Algorithm):
    def __init__(self):
        pass

    def run(self):
        pass