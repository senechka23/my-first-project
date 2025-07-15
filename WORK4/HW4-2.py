x = int(input("enter natural number: "))
count = 0
for i in range (1 , x + 1):
    if x % i == 0:
        count = count + 1
print(count)
