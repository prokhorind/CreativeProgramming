def for_each(lst, x):
    if len(lst) == x:
        return
    print(lst[x])
    for_each(lst, x + 1)




numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)

for_each(numbers, 0)
