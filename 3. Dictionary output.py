l1 = ["Ukraine", "Spain", "Italy"]
mydict = {(l1[0]): 'Kyiv', (l1[1]): 'Madrid', (l1[2]): 'Rome'}
for l2 in l1:
    print(f"{l2}: {mydict[l2]}")