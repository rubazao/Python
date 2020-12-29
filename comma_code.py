spam = ['cafe', 'cars', 'sugar', 'rice']


def comma_split(seq: list):
    if len(seq) <= 2:
        return (' and '.join(seq))
    else:
        return '{} and {}'.format(', '.join(seq[:-1]), seq[-1])


print(comma_split(spam))
