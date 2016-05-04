# Watson gives two integers (A and B) to Sherlock and
# asks if he can count the number of square integers
# between A and B (both inclusive).

import math

def find_square_integers(a, b):
    squares = 0
    for i in range(a, b+1):
        if math.sqrt(i) == math.floor(math.sqrt(i)):
            squares += 1

    return squares

def main():
    test_tuples = [(3, 9), (17, 24)]
    for tpl in test_tuples:
        print find_square_integers(*tpl)

if __name__ == '__main__':
    main()
