def linearize_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(linearize_list(item))
        else:
            result.append(item)
    return result
lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
print(linearize_list(lst))
