def answer2(l):
    d = {}
    for x in l:
        digit = [int(i) for i in x.split('.')]
        power = 2
        num = 0
        for y in digit:
            if y==0:
                num+=1
            num += y*(1000**power)
            power-=1
        d[num] = x
    result = []
    for key in sorted(d):
        print(key)
        result.append(d[key])
    return result
