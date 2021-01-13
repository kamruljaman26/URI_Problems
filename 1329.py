while True:
    N = int(input())
    if N == 0:
        break
    R = input().split()
    if len(R) == N:
        mary = 0
        john = 0
        for x in R:
            if x == "0":
                mary += 1
            elif x == "1":
                john += 1
        print("Mary won {} times and John won {} times".format(mary, john))
