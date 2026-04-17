def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b             # In general, a call to this function will evaluate
                                # this statement when a is the largest
    elif b > c:
        return b + c             # In general, a call to this function will evaluate
                                # this statement when b is larger than c
    else:
        return 2 * c             # In general, a call to this function will evaluate
                                # this statement when c is the largest


answer1 = function2(3, 2, 1)     # answer1 is 1
answer2 = function2(2, 3, 1)     # answer2 is 4
answer3 = function2(2, 1, 3)     # answer3 is 6
print(answer1, answer2, answer3)