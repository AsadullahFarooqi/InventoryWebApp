from

def list_changer(l):
    # """ if a list have tuple items and in those tuples there is only one item then this
    # function will return the list of only those items in the list the tuples will be gone."""
    # if len(l) > 0:
    #     return "sorry"
    #
    # else:
    z = []
    for i in l:
        z.append(i[0])

    return z
