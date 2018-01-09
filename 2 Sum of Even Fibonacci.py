#Find the sum of all even fibonacci numbers below 4,000,001
#Example 0,1,1,2,3,5,8,13 are all fib numbers below 20. Evens are 0,2,8. Sum to 10.

running_sum = 0
smaller_fib = 0
larger_fib = 1
maximum = 4000000

while larger_fib <= maximum:
    smaller_fib, larger_fib = larger_fib, smaller_fib+larger_fib
    if larger_fib % 2 == 0:
        running_sum += larger_fib
print(running_sum)
