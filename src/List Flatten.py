
def flatten(items):
    data = []
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, list):
            for sub_x in flatten(x):
                data.append(sub_x)
        else:
            data.append(x)
    return data


if __name__ == "__main__":
    a = [1,2,[3,[[[[[4,5,[[[[[6]]]]]]]]]]]]
    b = flatten(a)
    print(b)

