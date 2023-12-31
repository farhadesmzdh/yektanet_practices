from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def describeMe(self):
        pass

    def __init__(self):
        self.__clicks = 0
        self.__views = 0

    def getClicks(self):
        return self.__clicks

    def getViews(self):
        return self.__views

    def incClicks(self):
        self.__clicks += 1

    def incViews(self):
        self.__views += 1


