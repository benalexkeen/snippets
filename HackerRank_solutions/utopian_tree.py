# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height.
# Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring.
# How tall will her tree be after N growth cycles?

def height_after_n_growth_cycles(n):
    height = 1
    cycles = 0
    while cycles < n:
        if cycles % 2 == 1:
            height += 1
        else:
            height *= 2
        cycles += 1
    return height


def main():
    test_array = [0, 1, 4, 5, 10, 19, 31, 60]
    for i in test_array:
        print "Height after {} growth cycles is {}".format(i, height_after_n_growth_cycles(i))

if __name__ == '__main__':
    main()
