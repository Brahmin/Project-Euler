#Find the largest palindrome made from the product of two 3-digit numbers
#Example: The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

current_largest = 0

for number_one in range(999, 99, -1):
    for number_two in range(999, 99, -1):
        possible_palindrome = number_one * number_two
        #[::-1] uses slicing to reverse the list of characters
        if str(possible_palindrome) == str(possible_palindrome)[::-1] and possible_palindrome > current_largest:
            current_largest = possible_palindrome
            print(possible_palindrome)
