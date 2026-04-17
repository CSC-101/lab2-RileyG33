from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # For the first test it returns False
                                        # since 9 is not less than 3.
                     # For the second test it returns True because 2 >= 0 and less than 3
    if test:                            # This check is preventing an IndexError
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # The value of first is none
second = checked_access([1, 0, 1], 2)    # The value of second is 1
print(first, second)