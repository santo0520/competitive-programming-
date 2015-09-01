# naive method: generate fib sequence every time.
#better method : record even sum of fib sequence up to n
#heuristic : only 2,5,8,11...terms are even, can this be used for optimization?

def naive(n):
    """generate fib sequence <= n, return only even-valued terms"""
    a = 1
    b = 2
    result = []
    while b <= n:
        a,b = b,a+b
        if a%2 == 0:
            result.append(a)
    return result


#main
print "\n".join(str(sum(naive(int(raw_input())))) for i in xrange(int(raw_input())))
