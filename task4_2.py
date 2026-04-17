def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # This is calling to length_sum
                                       # (["this", "is", "the", "first", "call"])
    elif len(L) > 1:                                #  The value being added is 9
        result = len(L[0]) + len(L[1])  # This is calling to length_sum(["second call"])
    elif len(L) > 0:                            #   The value being added is 11
        result = len(L[0])        # This is calling to length_sum(["another", "call"])
    else:                                      # The value being added is 11
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)