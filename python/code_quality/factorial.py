def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n - 1)

#Get a
a = int(input())

# print f
print(f(a))