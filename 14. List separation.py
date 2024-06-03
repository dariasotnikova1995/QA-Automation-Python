list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
divisible_by_3 = [x for x in list if x % 3 == 0 and not x % 5 ==0]
divisible_by_5 = [y for y in list if y % 5 == 0 and not y % 3 ==0]
divisible_by_3_5 = [b for b in list if b % 3 == 0 and b % 5 == 0]
print("Numbers divisible by 3:", divisible_by_3)
print("Numbers divisible by 5:", divisible_by_5)
print("Numbers divisible by 3 and 5:", divisible_by_3_5)

