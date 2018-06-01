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

#result = powerSet(items)
#for i in range(2**len(items)):
#    print(next(result))

def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in either zero or one bags.

    Yields a tuple, (bag1, bag2), where each bag is a list of the items in that bag, ([], [])
    """
    N = len(items)
    for i in range(3**N):
        bag1 = []
        for j in range(N):
            if (i >> j) % 2 == 1:
                bag1.append(items[j])
        #Outside the j loop, we know a single bag1 combination
        #We need to look in bag one, make a subset of (items) that does not include items in (bag1), since duplicates are not allowed, and create the powerSet for bag 2 given bag 1.

        itemSubset = items.copy()
        if bag1 != []:
            for object in bag1:
                itemSubset.remove(object)
        
        M = len(itemSubset)
        for i in range(2**M):
            bag2 = []
            for j in range(N):
                if (i >> j) % 2 == 1:
                    bag2.append(itemSubset[j])
            yield (bag1, bag2)

result = yieldAllCombos(items)
for i in range(3**len(items)):
    print(next(result))

