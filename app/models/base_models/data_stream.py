from abc import ABC,abstractmethod


class DataStream(ABC):

    @abstractmethod
    def request(self,data):
        raise NotImplementedError

    @abstractmethod
    def display(self,data):
        raise NotImplementedError
