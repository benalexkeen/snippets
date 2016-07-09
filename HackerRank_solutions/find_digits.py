# Given an integer, N, traverse its digits and determine 
# how many digits evenly divide NN (i.e.: count the number 
# of times N divided by each digit ddi has a remainder of 0). 
# Print the number of evenly divisible digits.

# Sample Input:
# 12
# 1012

# Sample Output:
# 2
# 3

def find_digits(n):
    i = 0
    for digit in str(n):
        if int(digit) == 0:
            pass
        elif n % int(digit) == 0:
            i += 1

    return i


def main():
    test_list = [0, 12, 1012, 10712, 1032215]
    for i in test_list:
        print "Number of digits in {0} that {0} is divisible by is {1}".format(i, find_digits(i))


if __name__ == '__main__':
    main()
