#Find the smallest positive number that is evenly divisible by all numbers from 1-20.
#Example 2520 is the smallest number evenly divisible by 1 to 10.

top_number = 20
answer = 0
potential_answer = top_number

while answer == 0:
    for number in range(top_number, 1, -1):
        if potential_answer % number == 0:
            if number == 2:
                answer = potential_answer
                break
            continue
        else:
            break
    potential_answer += top_number
print(answer)
           
#Not all numbers between 2 and top_number need to be checked. Could be reduced.
