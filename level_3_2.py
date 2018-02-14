from itertools import combinations
def answer5(l):
    d = {}
    for n, x in enumerate(l):
        d[str(x)+str(n)] = []
    for n, x in enumerate(l):
        for m, y in enumerate(l):
            if y%x==0 and m>n:
                d[str(y)+str(m)].append(x)
    print(d)
    count = 0
    for x in d:
        for y in d[x]:
            count += len(d[y])
    return count
