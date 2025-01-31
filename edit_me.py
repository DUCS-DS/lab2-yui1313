
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    for i in range(1,len(lst)):
        if lst[i-1] < lst[i]:
            return (True)
        elif lst[i-1] > lst[i]:
            return (True)
        else:
            return (False)

testlst=[9,6,5,3,-11]
print(monotonic(testlst))