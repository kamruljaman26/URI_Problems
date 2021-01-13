N = int(input())
A, B, C, D, E = input().split(" ")
count = 0
for x in (A, B, C, D, E):
    x = int(x)
    if N == x:
        count += 1
print(count)
