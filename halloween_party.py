# Alex is attending a Halloween party with his girlfriend, Silvia. At the party, Silvia spots the corner of an infinite chocolate bar (two dimensional, infinitely long in width and length).

# If the chocolate can be served only as 1 x 1 sized pieces and Alex can cut the chocolate bar exactly  times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?

# Input Format 
# The first line contains an integer T, the number of test cases. T lines follow.
# Each line contains an integer K.

# Output Format
# T lines; each line should contain an integer that denotes the maximum number of pieces that can be obtained for each test case.

def number_of_cuts(K):
    if K % 2 == 0:
        a = K/2
        b = K/2
    else:
        a = (K-1)/2
        b = (K+1)/2
    return (a * b)


def main():
    test_cases = [5,6,7,8]
    for case in test_cases:
        print number_of_cuts(case)


if __name__ == '__main__':
    main()
