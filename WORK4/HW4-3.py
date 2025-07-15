a = int(input("enter number A: "))
b = int(input("enter number B (B >= A):"))
for i in range (a, b + 1):
    if i % 2 == 0:
        print(i, end='')