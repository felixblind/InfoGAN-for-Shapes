def count(n):
    i = 0
    for x1 in range(1,n + 1):
        for y2 in range(1,n + 1):
            for x2 in range(x1,n + 1):
                for y1 in range(y2, n + 1):
                    for x3 in range(x1, n + 1):
                        for y3 in range(y2, n + 1):
                            inLine = abs(x1-x2) == abs(x2-x3)
                            inLine = inLine or (abs(y1-y2) == abs(y2-y3))
                            if not inLine:
                                i = i  + 1
    return i

def count_doubles(n):
    i = 0
    for x1 in range(1,n + 1):
        for y2 in range(1,n + 1):
            for x2 in range(1,n + 1):
                for y1 in range(1, n + 1):
                    for x3 in range(1, n + 1):
                        for y3 in range(1, n + 1):
                            inLine = abs(x1-x2) == abs(x2-x3)
                            inLine = inLine or (abs(y1-y2) == abs(y2-y3))
                            if not inLine:
                                i = i  + 1
    return i
