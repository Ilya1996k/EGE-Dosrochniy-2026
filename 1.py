from itertools import permutations
s1 = "357 347 12567 26 13 34 123"
s2 = "AC BDF ADG EDF DG ACEGF BD"
s2 = {frozenset(x) for x in s2.split()}
p = permutations("ABCDEFG")
print(1,2,3,4,5,6,7)
for x in p:
    s3 = s1
    for i in zip("1234567", x):
        a, b = i
        s3 = s3.replace(a, b)
    s3 = {frozenset(x) for x in s3.split()}
    if s3 == s2:
        print(*x)