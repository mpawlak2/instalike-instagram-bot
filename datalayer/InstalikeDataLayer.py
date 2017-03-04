from abc import ABC, abstractmethod

import model


class InstalikeDataLayer(ABC):
    @abstractmethod
    def persist_user(self, user: model.User):
        pass
