# Given an array of integers, calculate
# which fraction of its elements are positive,
# which fraction of its elements are negative, and
# which fraction of its elements are zeroes,
# respectively.
# Print the decimal value of each fraction on a new line.

def plus_minus(arr):
    pos = neg = zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1

    pos /= float(len(arr))
    neg /= float(len(arr))
    zero /= float(len(arr))
    print pos
    print neg
    print zero

def main():
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr)

if __name__ == '__main__':
    main()
