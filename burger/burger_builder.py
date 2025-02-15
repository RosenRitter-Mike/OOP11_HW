from abc import abstractmethod, ABC
from typing import final

from burger import Burger


class BurgerBuilder(ABC):
    def __init__(self):
        self.__burger: Burger = None

    def get_burger(self):
        return self.__burger

    @final
    def build_burger(self):
        self.__burger = Burger()
        self.prepare_bun()
        self.prepare_veggies()
        self.prepare_main()
        self.prepare_gravy()
        self.prepare_side_dish()
        self.prepare_packaging()
        self.prepare_price()
        return self

    @abstractmethod
    def prepare_bun(self):
        raise NotImplementedError
    
    @abstractmethod
    def prepare_veggies(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_main(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def prepare_gravy(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_side_dish(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_packaging(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_price(self):
        raise NotImplementedError
