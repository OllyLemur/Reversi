from abc import ABC, abstractmethod

class Players(ABC):
    def __init__(self, value) -> None:
        self.value = value

    @abstractmethod
    def get_move(self):
        pass