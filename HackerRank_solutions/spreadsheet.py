# We know that spreadsheet applications use letters to name their columns.
# For example, the first column is labled 'A' and second is 'B'. Eventually, we get to 'Z',
# and then 'AA', 'AB', and so on.

# Let's write a function that, when given the name of a column, returns its index. So 'A'
# would return 1, 'B' would return 2, 'Z' would return 26 and 'AA' would return 27.
import re

def get_index(_str):
    assert re.match(r'[A-Z]+', _str)
    index = 0
    base = 26
    for i in range(len(_str)):
        power = len(_str) - (i + 1)
        character_num = ord(_str[i]) - 64
        index += (base ** power) * character_num

    return index


def main():
    test_cases = ['A', 'Z', 'AA', 'AZ', 'ZZ', 'AAA', 'ZZZ', 'BBB',]
    for case in test_cases:
        print 'The index of {} is {}'.format(case, get_index(case))


if __name__ == '__main__':
    main()
