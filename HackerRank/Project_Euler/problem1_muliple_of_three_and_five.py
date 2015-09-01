def sum_one_to_n(n):
    return (1+n)*n/2
#failed due to overtime. can we do better? Instead odf o(n)
def sum_of_multiples_of_three_and_five_iterative(n):
    return str(sum( i for i  in range(n) if (i %3 ==0 or i % 5 == 0) ))

#constant time
def sum_of_multiples_of_three_and_five_constant_time(n):
    return sum_one_to_n(n/3)*3 + sum_one_to_n(n/5)*5 - sum_one_to_n(n/15)*15
#main
print "\n".join(str(sum_of_multiples_of_three_and_five_constant_time(int(raw_input())-1))for i in xrange(int(raw_input())))

