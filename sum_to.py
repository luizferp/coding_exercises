def sum_to(value, elements):
    h_els = {}

    for el in elements:
        if h_els.get(value-el):
            return True
        h_els.update({el: value})

    return False


print(sum_to(42, [1,2,3,4,5,6,7,40,9]))
