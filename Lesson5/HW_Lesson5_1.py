#lst = [1, 2, 4, 5, 6, 7, 8, 100]
#lst = [1, 3, 5]
#lst = [6]
lst = []
if len(lst) != 0:
    y = lst[-1]
    new_lst = lst[::2]
    print(y)
    z = sum(new_lst)
    print(z * y)
else:
    print(lst)



