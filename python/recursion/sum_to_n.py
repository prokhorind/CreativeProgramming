def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)



def sum_to_n_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

#print(sum_to_n(1000))
print(sum_to_n_iterative(1000))
