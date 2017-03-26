from abc import ABC, abstractmethod


class MediaAlgorithm(ABC):
    @abstractmethod
    def get_media(self):
        pass


class TagMediaAlgorithm(MediaAlgorithm):
    __tag_list = []

    def __init__(self, tag_list):
        self.__tag_list = tag_list

    def get_media(self):
        pass


class ContentManager:
    __media_list = []
    __media_algorithm = None

    def get_media_generator(self):
        if not self.__media_list:
            self.download_media()

        yield self.__media_list.pop()

    def download_media(self):
        self.__media_list = self.__media_algorithm.get_media()
