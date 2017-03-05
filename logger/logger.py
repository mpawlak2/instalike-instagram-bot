from abc import ABC, abstractmethod


class Logger(ABC):
    def log(self, message):
        pass