x = lambda a, b, c: a + b + c
y = lambda a, b: ((a * a) + (b * b))
z = lambda a, b, c, d, e: (a + b + c + d) - e


n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

print("\n\n")

print(x(n1, n2, n3))
print(y(n1, n2))
print(z(n1, n2, n3, n4, n5))
