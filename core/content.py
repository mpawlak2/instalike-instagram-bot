from abc import ABC, abstractmethod


class MediaAlgorithm(ABC):
    @abstractmethod
    def get_media(self):
        pass


class TagMediaAlgorithm(MediaAlgorithm):
    __tag_list = []
    __operations = None

    def __init__(self, tag_list, operations):
        self.__tag_list = tag_list
        self.__operations = operations

    def get_media(self):
        media_list = []
        tag = self.__tag_list.pop()


class ContentManager:
    __media_list = []
    __media_algorithm = None
    __media_generator = None

    def get_next_media(self):
        if self.__media_generator is None:
            self.__media_generator = self.get_media_generator()

        return next(self.__media_generator)

    def get_media_generator(self):
        if not self.__media_list:
            self.download_media()

        yield self.__media_list.pop()

    def download_media(self):
        self.__media_list = self.__media_algorithm.get_media()
