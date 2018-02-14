def answer3(l):
    if len(l)==2:
        if (l[1]-l[0])%3 == 0:
            return [2*(l[1]-l[0])//3,1] if (l[1]-l[0])//3>=1 else [-1,-1]
        else:
            return [2*(l[1]-l[0]),3] if (l[1]-l[0])/3>=1 else [-1,-1]
    i = -2*l[1]+(l[0]+l[2])
    mul = 1
    for x in range(3,len(l)):
        i = l[x]-l[x-1]-i
        mul = mul*(-1)
    a = l[::-1]
    r = Fraction(i,(1-mul*2))
    print(r)
    for x in range(0,len(a)-1):
        if r<1:
            return [-1,-1]
        r = (a[x]-a[x+1])-r
        print(r)
    if 2*i%(1-mul*2)==0:
        return [2*i//(1-mul*2),1] if 2*i//(1-mul*2)>=1 else [-1,-1]
    else:
        if (1-mul*2)>0:
            return [2*i,(1-mul*2)] if 2*i/(1-mul*2)>=1 else [-1,-1]
        else:
            return [-2*i,-(1-mul*2)] if 2*i/(1-mul*2)>=1 else [-1,-1]
