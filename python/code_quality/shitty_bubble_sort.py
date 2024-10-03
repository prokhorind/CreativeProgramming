def s(l):
    for i in range(len(l)):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

a = [64, 34, 25, 12, 22, 11, 90]
print(s(a))