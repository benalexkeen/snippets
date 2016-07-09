# Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

def diagonal_difference(matrix, n):
    forward_diagonal = 0
    backward_diagonal = 0
    for i in range(n):
        forward_diagonal += matrix[i][i]
        backward_diagonal += matrix[i][n-(i+1)]

    print abs(forward_diagonal - backward_diagonal)

def main():
    a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    # 11   2   4
    #  4   5   6
    # 10   8 -12
    diagonal_difference(a, 3)

if __name__ == '__main__':
    main()
