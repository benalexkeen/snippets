"""There are two kangaroos on an x-axis 
ready to jump in the positive direction (i.e, toward positive infinity). 
The first kangaroo starts at location x1 and moves at a 
rate of v1 meters per jump. The second kangaroo starts at location x2 
and moves at a rate of v2 meters per jump. 
Given the starting locations and movement rates for each kangaroo, 
can you determine if they'll ever land at the same location at the same time?
0 <= x1 < x2 < 10000
1 <= v1 <= 10000
1 <= v2 <= 10000
Print YES if they can land on the same location at the same time; otherwise, print NO.
"""

def next_jump(x1, v1, x2, v2):
    pos1 = x1 + v1
    pos2 = x2 + v2
    return pos1, pos2

def kangaroos_meet(x1, v1, x2, v2):
    if (v2 > v1) or (v1 == v2):
        return "NO"
    while x1 < x2:
        x1, x2 = next_jump(x1, v1, x2, v2)
        if x1 == x2:
            return "YES"
    return "NO"

def __main__():
    print kangaroos_meet(0, 3, 4, 2)

if __name__ == '__main__':
    __main__()
