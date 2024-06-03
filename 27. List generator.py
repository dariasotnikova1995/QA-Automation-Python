def list_item_generator(lst, iter_num=None):
    if iter_num is None:
        while True:
            yield from lst
    else:
        count = 0
        while True:
            yield lst[count % len(lst)]
            count += 1
            if count % len(lst) == 0 and iter_num != 0:
                iter_num -= 1
            if iter_num == 0:
                break
lst = ['a', 'b']
for i in list_item_generator(lst, iter_num=2):
    print(i)