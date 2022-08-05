from abc import ABC, abstractmethod

class Players(ABC):

    @abstractmethod
    def choose_move(self):
        pass