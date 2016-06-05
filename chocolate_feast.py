# Little Bob loves chocolate, and he goes to a store with $N in his pocket. 
# The price of each chocolate is $C. 
# The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. 
# How many chocolates does Bob get to eat?

def offer(M, wrappers):
    return wrappers // M


def chocolate_feast(money, price, discount_M):
    chocolates_bought = money // price
    free_chocolates = offer(discount_M, chocolates_bought)
    total_wrappers = chocolates_bought + free_chocolates
    total_chocolates = chocolates_bought + offer(discount_M, total_wrappers)
    return total_chocolates


def main():
    test_cases = [
        (10,2,5),
        (12,4,4),
        (6,2,2)
    ]
    for case in test_cases:
        print chocolate_feast(*case)


if __name__ == '__main__':
    main()
