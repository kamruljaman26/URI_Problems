import sys

while sys.stdin:
    try:
        x, y = input().split(" ")
        x = int(x)
        y = int(y)
        if x<y:
            print((y - x))
        else:
            print((x - y))
    except EOFError:
        break
