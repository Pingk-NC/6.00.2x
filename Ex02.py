#! Python3

#Making a fibonacci generator using a memoised recursive function
def fast_fib(fib_num, memo = {}):
    """
    Recursively computes the n-th fibonacci number, where n is fib_num.
    fib_num is assumed to be a positive integer.
    memo need not be used by the user, it is used to store results from recurvise calls.
    """
    if fib_num <= 1:
        return 1
    elif fib_num in memo:
        return memo[fib_num]
    else:
        result = fast_fib(fib_num-1, memo) + fast_fib(fib_num-2, memo)
        memo[fib_num] = result
        print(memo)
        return result

print(fast_fib(9))
