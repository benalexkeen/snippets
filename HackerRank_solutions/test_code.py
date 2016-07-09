#!/bin/python

import sys

def offer(M, wrappers):
    return wrappers // M


def chocolate_feast(money, price, discount_M):
    chocolates_bought = money // price
    free_chocolates = offer(discount_M, chocolates_bought)
    total_wrappers = chocolates_bought + free_chocolates
    total_chocolates = chocolates_bought + offer(discount_M, total_wrappers)
    return total_chocolates


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    print chocolate_feast(n,c,m)