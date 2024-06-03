lst = [1, 2, 3, 4, 5]
new_lst = []
for i in range(len(lst) - 1):
    new_lst.append(lst[i])
    new_lst.append((lst[i] + lst[i + 1]) / 2)
new_lst.append(lst[-1])
print(new_lst)