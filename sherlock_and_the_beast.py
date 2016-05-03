# Sherlock determines the key to removing the virus
# is to find the largest Decent Number having N digits.

# A Decent Number has the following properties:

# Its digits can only be 3's and/or 5's.
# The number of 3's it contains is divisible by 5.
# The number of 5's it contains is divisible by 3.
# If there are more than one such number, we pick the largest one.


def decent_number(n):
    number_of_5s = 0
    number_of_3s = 0
    while n > 0:
        if n % 3 == 0:
            number_of_5s += n
            n = 0
            break
        n -= 5
        number_of_3s += 5

    if n == 0:
        return "5" * number_of_5s + "3" * number_of_3s
    elif n < 0:
        return "-1"

def main():
    test_array = [1, 3, 4, 5, 11, 19, 10000]
    for i in test_array:
        print "Highest Decent Number of Length {} is {}".format(i, decent_number(i))

if __name__ == '__main__':
    main()
