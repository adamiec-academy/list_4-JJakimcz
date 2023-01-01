def min_max(data):
    minimum=data(1)
    maximum=data(1)

    for l in len(data):
        if l<minimum:
            minimum=l
        if l>maximum:
            maximum=l

    return minimum, maximum
