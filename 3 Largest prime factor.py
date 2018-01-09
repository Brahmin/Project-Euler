#Find the largest prime factor of 600851475143
#Example: The prime factors of 13195 are 5,7,13,29. Largest being 29.
import math

number_to_factor = 600851475143
winner = 0

for possible_prime_factor in range(2, math.ceil(math.sqrt(number_to_factor))):
    if number_to_factor % possible_prime_factor == 0:
        #This puts the factor and the corresponding factor into a tuple. Larger first.
        matching_factors = number_to_factor / possible_prime_factor, possible_prime_factor
        for factor in matching_factors:
            rounded_sqrt_of_possible_prime = math.ceil(math.sqrt(factor))
            for prime_tester in range(2, rounded_sqrt_of_possible_prime):
                if factor % prime_tester == 0:
                    print(factor)
                    print('Factor, but not prime above')
                    break
                #If we go through the whole possibility space without a factor, number is prime.
                elif prime_tester == rounded_sqrt_of_possible_prime-1:
                    print(factor)
                    print('A prime factor above')
                    if factor > winner:
                        winner = possible_prime_factor
if winner == 0:
    print('Number is prime')
else:
    print(winner)
