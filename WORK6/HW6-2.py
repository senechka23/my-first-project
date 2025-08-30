n = int(input())

arr = list(map(int, input().split()))

result = []

result.append(arr[-1])

for i in range(n-1):
    result.append(arr[i])

print(*result)