from typing import override

from burger_builder import BurgerBuilder


class CrispyChickenBuilder(BurgerBuilder):

    def prepare_bun(self):
        self.get_burger().prepare_bun("Ciabatta bun\n")

    @override
    def prepare_veggies(self):
        self.get_burger().prepare_veggies("Frash crispy Lattice, thin slices of Tomato, onion and frash basil\n")

    @override
    def prepare_main(self):
        self.get_burger().prepare_main("Crispy chicken\n")

    @override
    def prepare_gravy(self):
        self.get_burger().prepare_gravy("Pesto with nuts and garlic\n")

    @override
    def prepare_side_dish(self):
        self.get_burger().prepare_side_dish("A mix of french fries and sweet potato fries\n")

    @override
    def prepare_packaging(self):
        self.get_burger().prepare_packaging("The burger is wrapped in paper, the fries in a box, "
                                            "a box containing 2 spiced mayo, 2 ketchup, 2 bbq small bags. "
                                            "\nAll inside a cardboard box with the company loggo and an Italian flag "
                                            "a chicken in a mafia suit holding a tommy gun cricature "
                                            "and the writing 'Chicken Genovese'\n")

    @override
    def prepare_price(self):
        self.get_burger().prepare_price("An offer you cannot refuse 65.90\n"
                                        "i see you are a man of culture, would you like a glass of chianti with that\n")
