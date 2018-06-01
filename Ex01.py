#! python3

def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N): #32 iterations
        combo = []
        for j in range(N): #1 to 5
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo 

items = ['1', '10', '100', '1,000', '10,000']

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in either zero or one bags.

    Yields a tuple, (bag1, bag2), where each bag is a list of the items in that bag, ([], [])
    """
    N = len(items)
    for i in range(2**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i >> j) % 2 == 1:
                bag1.append(items[j])
        
        M = len(bag1)
        if i == 0:
            for j in range(N):
                bag2.append(items[j])
        yield (bag1, bag2)

result = yieldAllCombos(items)
for i in range(2**len(items)):
    print(next(result))

