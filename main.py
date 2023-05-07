from itertools import combinations as cb
from math import ceil
from collections import Counter

class Calculator:
    def __init__(self, mylist: list, length_of_one_piece: float, minimum_acceptable_length: float, add_ten_percent: bool = False):
        self.mylist = mylist
        self.target = length_of_one_piece
        self.best_so_far = self.target
        self.minimum_acceptable_length = minimum_acceptable_length
        self.add_ten_percent = add_ten_percent
        self.count = 0
    def divide_long_items(self):
        values_to_remove = []
        for item in self.mylist:
            if item > self.target:
                temp = item
                while temp >= self.target:
                    self.mylist.append(self.target)
                    temp = temp - self.target
                if temp > 0:
                    self.mylist.append(temp)
                values_to_remove.append(item)
        self.mylist = [x for x in self.mylist if x not in values_to_remove] # remove the bigger parts from the list

    def calculate(self):
        self.how_many_do_you_need()
        self.divide_long_items()
        while self.mylist:
            self.calculate_best_combination()

    def remove_from_list(self, items_to_remove: list) -> list:
        self.mylist = list((Counter(self.mylist)-Counter(items_to_remove)).elements())
        self.best_so_far = self.target
        return self.mylist

    def calculate_best_combination(self):
        for i in range(1, len(self.mylist)+1):
            comb = cb(self.mylist[::-1], i)
            for items in comb:
                if sum(items) <= self.target:
                    if sum(items) == self.target:
                        self.count += 1
                        print(f'{self.count}. {list(items)}')
                        self.remove_from_list(list(items))
                        return
                    elif sum(items) <= self.target:
                        if self.best_so_far > self.target - sum(items): # find the closest combination to the target length
                            self.best_so_far = self.target - sum(items)
                            best_combination = items    # for printing
        self.count += 1
        print(f'{self.count}. {list(best_combination)} = {sum(best_combination)}')
        self.remove_from_list(list(best_combination))

    def how_many_do_you_need(self) -> int:
        if self.add_ten_percent:
            multiplier = 1.1
        else:
            multiplier = 1
        print(f'You need {ceil(sum(self.mylist) / self.target * multiplier)} items to cover everything')
        return ceil(sum(self.mylist) / self.target * multiplier)


if __name__ == "__main__":
    calc = Calculator([5.2, 1.2, 3.3], 2.4, 0.50, True)
    calc.calculate()
