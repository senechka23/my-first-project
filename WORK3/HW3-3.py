sum = int(input("min sum investment: "))
Mike = int(input("how many dollars does Mike have: "))
Ivan = int(input("how many dollars does Ivan have: "))

if Mike >= sum and Ivan >= sum:
    print(2)
elif Mike >= sum:
    print(Mike)
elif Ivan >= sum:
    print(Ivan)
elif Mike + Ivan >= sum:
    print(1)
else:
    print(0)