from typing import override

from burger_builder import BurgerBuilder


class BeyondBuilder(BurgerBuilder):

    def prepare_bun(self):
        self.get_burger().prepare_bun("Whole grain bun with caraway seeds\n")

    @override
    def prepare_veggies(self):
        self.get_burger().prepare_veggies("Frash crispy Lattice, Traditional tabouli salad\n")

    @override
    def prepare_main(self):
        self.get_burger().prepare_main("Beyond beef burger\n")

    @override
    def prepare_gravy(self):
        self.get_burger().prepare_gravy("garlic aioli\n")

    @override
    def prepare_side_dish(self):
        self.get_burger().prepare_side_dish("Thai Cabbage Salad\n")

    @override
    def prepare_packaging(self):
        self.get_burger().prepare_packaging("The burger is wrapped in paper, the salad in a closed plastic bowl, "
                                            "a box containing 2 spiced mayo, 2 ketchup, and 2 balsamic vinegar bags. "
                                            "\nAll inside a cardboard box with the company loggo "
                                            "a cow in buddhist monk robes caricature and the writing 'Holy Cow'\n")

    @override
    def prepare_price(self):
        self.get_burger().prepare_price("A truly devine  offer 55.90\n"
                                        "goes heavenly well with some freshly squeezed lime juice\n")
