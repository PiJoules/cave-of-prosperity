#!/usr/bin/env python 

from BetterThanMandy import BetterThanMandy

limit = float(raw_input())
nugget_count = int(raw_input())
nuggets = []
for i in range(nugget_count):
	nuggets.append(float(raw_input()))

btm = BetterThanMandy(limit, nuggets)
btm.print_backpack_weight()
btm.print_nuggets()