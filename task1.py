def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([1, 1]) == 1.0
assert average_num([2.5, 3.5]) == 3.0
assert average_num([1, 2, 3, 4, 5]) == 3.0
assert average_num([1.1, 2.2, 3.3]) == 2.2
assert average_num([10, 20, 30]) == 20.0
assert average_num([]) == "Bad request"
assert average_num([1, 'a']) == "Bad request"
assert average_num([1, 2, '3']) == 2.0
assert average_num([1,2, 'abc']) == "Bad request"
assert average_num([1.5, 2.5, 3.5, '4.5']) == 3.0
