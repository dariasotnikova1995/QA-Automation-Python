def second_largest_number(numbers):
    if len(set(numbers)) <= 1:
        return None
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest
print(second_largest_number([]))
print(second_largest_number([1, 1]))
print(second_largest_number([1, 2, 3, 4, 5]))