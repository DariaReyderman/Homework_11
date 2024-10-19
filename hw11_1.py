import random

list1: list[bool] = [random.choice([True, False]) for _ in range(3)]
print('a', list1)
print('b', list1, "The list contains only 'True':", all(list1))
print('c', list1, "The list contains at least one 'True':", any(list1))
print('d', list1, "The list contains only 'False':", not any(list1))
print('e', list1, "The list contains at least one 'False':", not all(list1))

list2: list[int] = [random.randint(-2, 2) for _ in range(5)]
print('f', list2)
if all([number != 0 for number in list2]):
    print('g', list2, "Yes, the list contains only non-zero numbers")
else:
    print('g', list2, "No, the list contains zero")
if any([number != 0 for number in list2]):
    print('h', list2, "Yes, there is at least one non-zero number")
else:
    print('h', list2, "No, all numbers in this list are zeros")
if all([number == 0 for number in list2]):
    print('i', list2, "Yes, all numbers are zeros")
else:
    print('i', list2, "No, there is non-zero numbers")
if any([number == 0 for number in list2]):
    print('j', list2, "Yes, there is at least one zero in this list")
else:
    print('j', list2, "The list doesn't contain zeros")
