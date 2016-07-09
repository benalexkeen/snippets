# Calvin is driving his favorite vehicle on the 101 freeway. 
# He notices that the check engine light of his vehicle is on, 
# and he wants to service it immediately to avoid any risks. 
# Luckily, a service lane runs parallel to the highway. 
# The length of the service lane is  N units. 
# The service lane consists of N segments of equal length and different width.

# Calvin can enter to and exit from any segment. 
# Let's call the entry segment as index i and the exit segment as index j. 
# Assume that the exit segment lies after the entry segment (i <= j) and (0 <= i). 
# Calvin has to pass through all segments from index  to index  (both inclusive).

# Calvin has three types of vehicles - bike, car, and truck - represented by 1, 2 and 3, respectively. 
# These numbers also denote the width of the vehicle.

# You are given an array width of length N, where width[k] represents the width of the kth segment of the service lane. 
# It is guaranteed that while servicing he can pass through at most  segments, 
# including the entry and exit segments.

# Given the entry and exit point of Calvin's vehicle in the service lane, 
# output the type of the largest vehicle which can pass through the service lane (including the entry and exit segments).

def max_width_vehicle(width_array, i, j):
    width_array = width_array[i:(j+1)]
    return min(width_array)


def main():
    width_array = [2, 3, 1, 2, 3, 2, 3, 3]
    test_cases = [(0, 3), (4, 6), (6, 7), (3, 5), (0, 7)]
    for case in test_cases:
        print max_width_vehicle(width_array, *case)


if __name__ == '__main__':
    main()
