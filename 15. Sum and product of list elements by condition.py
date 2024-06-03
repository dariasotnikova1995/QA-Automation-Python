lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6
filtered_list = [x for x in lst if MIN <= x <= MAX]
if filtered_list:
    sum = sum(filtered_list)
    product = 1
    for num in filtered_list:
        product *= num
else:
    sum = None
    product = None
print("sum =", sum, ", product =", product)