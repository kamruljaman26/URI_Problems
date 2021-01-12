while True:
    try:
        N = int(input())
        for i in range(N):
            for j in range(N):
                if (i + j == N - 1):
                    print("2", end="")
                elif (i == j):
                    print("1", end="")
                else:
                    print("3", end="")
            print("")
    except EOFError:
        break
