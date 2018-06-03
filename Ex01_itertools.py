#! Python3
from itertools import chain, combinations

def power_set(items):
    """
    Creates a powerset for all objects in items
    items is an iterable set of objects to create the powerset with
    yields a tuple where each bag is a list of objects
    """

    #combinations takes the initial set and the bag size
    #bag_size tells combinations to find all combinations of items for a bag size of X
    #The list comprehension increments bag_size to achieve a full powerset.
    for subset in chain.from_iterable(combinations(items, bag_size) for bag_size in range(len(items) + 1)):
        yield subset

items = ['1', '10', '100']

#result = power_set(items)
#for i in range(2**len(items)):
#    print(next(result))

#This is an alternate solution to the 2-bag problem
def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
#result = yieldAllCombos(items)
#for i in range(3**len(items)):
#    print(next(result))

#This is an alternate solution to the power_set that uses recursion
def powerset_rec(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset_rec(seq[1:]):
            yield [seq[0]]+item
            yield item

result = powerset_rec(items)
for i in range(2**len(items)):
    print(next(result))
