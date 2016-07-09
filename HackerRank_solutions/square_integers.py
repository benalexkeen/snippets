# Watson gives two integers (A and B) to Sherlock and
# asks if he can count the number of square integers
# between A and B (both inclusive).

import math

def find_square_integers(a, b):
    bottom_sqrt_int = math.ceil(math.sqrt(a))
    top_sqrt_int = math.floor(math.sqrt(b))
    return int(top_sqrt_int - bottom_sqrt_int + 1)

def main():
    test_tuples = [(3, 9), (17, 24)]
    for tpl in test_tuples:
        print find_square_integers(*tpl)

if __name__ == '__main__':
    main()
