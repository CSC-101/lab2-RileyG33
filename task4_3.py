def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
# The value of words is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
# The values of both first and second is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
# When "words" is passed into "surprising" the local variable L
# points to the same thing as "words". The .append() method modifies
# the list in place. So every time the function is called, it updated the original
# "words" list. Since the function return L, both first and second are assigned the same original
# list object. They are all aliases
print(words, first, second)