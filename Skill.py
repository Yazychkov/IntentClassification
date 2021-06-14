from abc import ABCMeta, abstractmethod


class Skill(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def load_data(self) -> None:
        pass

    @abstractmethod
    def get_answer(self, phrase, context=None) -> str:
        pass
