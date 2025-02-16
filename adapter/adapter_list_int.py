from data_holder import DataHolder
from factorial_calc import FactorialCalculator


class AdapterList2Int:

    def calc_factorial(self, num_list):
        # convert
        int_list = [int(num) for num in num_list]

        # execute
        return [FactorialCalculator().calc_factorial(num) for num in int_list]
