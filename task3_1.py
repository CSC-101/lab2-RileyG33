def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # It is evaluated for none of them,
                        # both calls are false so they execute the "else" statement
    else:
        return m

first = smallest(3, 2)       # The value of first is 2
second = smallest(2, 2)      # The value of second is 2.
                                    # This is reasonable because both numbers are two
                                    # so either one can be the "smallest"
print(first,second)