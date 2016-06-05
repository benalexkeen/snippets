# You are given N sticks, where the length of each stick is a positive integer. 
# A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

# Suppose we have six sticks of the following lengths:
# 5 4 4 2 2 8

# Then, in one cut operation we make a cut of length 2 from each of the six sticks. 
# For the next cut operation four sticks are left (of non-zero length), whose lengths are the following: 
# 3 2 2 6

# The above step is repeated until no sticks are left.

# Given the length of  sticks, print the number of sticks that are left before each subsequent cut operations.

# Note: For each cut operation, you have to recalcuate the length of smallest sticks (excluding zero-length sticks).

def cut_the_sticks(array):
    if len(array) == 0:
        return None
    print len(array)
    _min = min(array)
    new_array = [i-_min for i in array if i-_min != 0]
    cut_the_sticks(new_array)


def main():
    test_cases = [
        [5,4,4,2,2,8],
        [1,2,3,4,3,3,2,1]
    ]

    for case in test_cases:
        cut_the_sticks(case)


if __name__ == '__main__':
    main()
