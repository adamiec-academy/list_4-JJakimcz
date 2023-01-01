def min_max(data):
    minimum=data[0]
    maximum=data[0]

    for l in data:
        if l<minimum:
            minimum=l
        elif l>maximum:
            maximum=l

    return minimum, maximum
