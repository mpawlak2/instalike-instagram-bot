from abc import ABC, abstractmethod


class MediaAlgorithm(ABC):
    @abstractmethod
    def get_media(self):
        pass


class TagMediaAlgorithm(MediaAlgorithm):
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
