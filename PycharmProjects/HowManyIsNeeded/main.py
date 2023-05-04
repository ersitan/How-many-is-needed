from itertools import combinations as cb
from math import ceil
from collections import Counter


class Calculator:
    def __init__(self, mylist: list, target: float):
        self.mylist = mylist
        self.target = target
        self.best_so_far = self.target

    def calculate(self):
        self.how_many_do_you_need()
        for item in self.mylist:
            if item > self.target:
                division = ceil(item / self.target)
                for i in range(division):
                    self.mylist.append(item / division)
                self.mylist.remove(item)

        while self.mylist:
            self.calculate_best_combination()

    def remove_from_list(self, items_to_remove: list) -> list:
        self.mylist = list((Counter(self.mylist)-Counter(items_to_remove)).elements())
        self.best_so_far = self.target
        return self.mylist

    def calculate_best_combination(self):
        for i in range(len(self.mylist)+1):
            comb = cb(self.mylist[::-1], i)
            for items in comb:
                if sum(items) == self.target:
                    print(f'{items} is the best combination')
                    self.remove_from_list(list(items))
                    return
                elif sum(items) <= self.target:
                    # print(f'{items} sum: {sum(items)}')
                    if self.best_so_far > self.target - sum(items):
                        self.best_so_far = self.target - sum(items)
                        best_combination = items

        print(f'best_combination: {best_combination} = {sum(best_combination)}')
        self.remove_from_list(list(best_combination))

    def how_many_do_you_need(self, with_ten_percent: bool = True) -> int:
        if with_ten_percent:
            multiplier = 1.1
        else:
            multiplier = 1
        print(f'You need {ceil(sum(self.mylist) / self.target * multiplier)} items to cover everything')
        return ceil(sum(self.mylist) / self.target * multiplier)


if __name__ == "__main__":
    calc = Calculator([2.44, 0.37, 0.71, 1.2, 3.7, 0.76], 2.44)
    calc.calculate()
