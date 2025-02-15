from crispy_chicken_builder import CrispyChickenBuilder
from byeond_builder import BeyondBuilder
from burger import Burger
from home_burger_builder import HomeBurgerBuilder

if __name__ == "__main__":
    crispy_chicken: Burger = CrispyChickenBuilder().build_burger().get_burger()
    print(crispy_chicken)

    beyond: Burger = BeyondBuilder().build_burger().get_burger()
    print(beyond)

    home_burger = HomeBurgerBuilder().build_burger().get_burger()
    print(home_burger)