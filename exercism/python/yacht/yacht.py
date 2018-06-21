from collections import Counter
# Score categories # Change the values as you see fit
maxCount = (lambda dice: max(Counter(dice).values()))

YACHT = (lambda dice:  50 if len(set(dice)) == 1 else 0)
ONES =  (lambda string: calc_sum_of_string(string, 1))
TWOS = (lambda string: calc_sum_of_string(string, 2))
THREES = (lambda string: calc_sum_of_string(string, 3))
FOURS =  (lambda string: calc_sum_of_string(string, 4))
FIVES = (lambda string: calc_sum_of_string(string, 5))
SIXES = (lambda string: calc_sum_of_string(string, 6))
FULL_HOUSE = (lambda string: calc_full_house(string) if maxCount(string) == 3 else 0)
FOUR_OF_A_KIND = (lambda dice: calc_four_of_a_kind(dice))
LITTLE_STRAIGHT = (lambda dice: 30 if list(range(1,6)) == dice else 0) 
BIG_STRAIGHT = (lambda dice: 30 if list(range(2,7)) == dice else 0)
CHOICE =  (lambda dice: sum(map(int, dice)))

def calc_sum_of_string(dice, condition):
    return sum(filter_dice_with_number(dice, condition))

def filter_dice_with_number(dice, condition):
    return list(filter((lambda number: number == condition), dice)) 
 
def calc_full_house(dice):
    numbers = list(set(dice))
    return sum(filter_dice_with_number(dice, numbers[0])) + sum(filter_dice_with_number(dice, numbers[1]))
    
def calc_four_of_a_kind(x):
    four_times_elements = [dice for dice in set(x) if x.count(dice) >= 4]
    return 4*four_times_elements[0] if len(four_times_elements) > 0 else 0

def score(dice, category):
    return category(sorted(dice))
