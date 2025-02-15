class Burger:
    def __init__(self):
        self.ingredients = []

    def prepare_bun(self, bun):
        self.ingredients.append(bun)

    def prepare_veggies(self, vegg):
        self.ingredients.append(vegg)

    def prepare_main(self, main):
        self.ingredients.append(main)

    def prepare_gravy(self, gravy):
        self.ingredients.append(gravy)

    def prepare_side_dish(self, side):
        self.ingredients.append(side)

    def prepare_packaging(self, pack):
        self.ingredients.append(pack)

    def prepare_price(self, price):
        self.ingredients.append(price)

    def __str__(self):
        return "Burger Ingredients: " + ", ".join(self.ingredients)