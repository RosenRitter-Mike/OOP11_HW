from typing import override

from burger_builder import BurgerBuilder


class HomeBurgerBuilder(BurgerBuilder):

    def prepare_bun(self):
        self.get_burger().prepare_bun("Soft and silky buns, a bit roasted for taste\n")

    @override
    def prepare_veggies(self):
        self.get_burger().prepare_veggies("Frash crispy Lattice, thin slices of hot chilli, red onions "
                                          "and grilled pineapple\n")

    @override
    def prepare_main(self, **kwargs):
        self.get_burger().prepare_main("2 Juicy lamb burgers with a slice of Hverti cheese between them"
                                       "and a slices of cheddar on top and underneath\n")

    @override
    def prepare_gravy(self):
        self.get_burger().prepare_gravy("Sriracha mayo and guacamole mix\n")

    @override
    def prepare_side_dish(self):
        self.get_burger().prepare_side_dish("Coleslaw with peanuts in miso souse and "
                                            "Szechuan smashed cucumber salad\n")

    @override
    def prepare_packaging(self):
        self.get_burger().prepare_packaging("The burger is wrapped in paper, the salads in 2 small closed plastic bowls"
                                            "a box containing 2 spiced mayo, 2 ketchup, 2 bbq, 2 balsamic vinegar bags."
                                            "\nAll inside a cardboard box with the company loggo and an hawaiian flag "
                                            "a lamb in a surfer suit and sunglasses holding a serfing board cricature "
                                            "and the writing 'Home Lamb'\n")

    @override
    def prepare_price(self):
        self.get_burger().prepare_price("Dude check out this offer 71.90\n"
                                        "with a glass of pale ale this would be awsome\n")
