def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()


def border_map(a, b):
    m=[["." for _ in range(a)] for _ in range(b)]
    
    for x in range(b):
        m[x][0] = "X"
        m[x][a-1] = "X"

    for y in range(a):
        m[0][y] = "X"
        m[b-1][y] = "X"

    return m
