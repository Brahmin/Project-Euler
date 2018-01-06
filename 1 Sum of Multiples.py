#Find the sum of all multiples of 3 or 5 below 1000.
#Example: 3, 5, 6, 9 are all multiples below 10. Sum to 23.

running_sum = 0
multiples_matter = 3, 5

for number in range(1,1000):
    for each in multiples_matter:
        if number % each == 0:
            running_sum += number
            break
        
print(running_sum)
