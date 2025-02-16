from data_holder import DataHolder
from factorial_calc import FactorialCalculator


class AdapterFloat2Int:

    def calc_factorial(self, float_number):
        # convert
        int_number = int(float_number)

        # execute
        return FactorialCalculator().calc_factorial(int_number)



