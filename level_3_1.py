from math import log
def answer4(n):
    n = int(n);
    step = 0;
    while n!=1:
        if n%2==0:
            n = n//2
            step = step + 1
        else:
            add = n + 1
            minus = n - 1
            p_add = 0
            p_minus = 0
            while(True):
                # add if add
                if add%2==1 and minus%2==1:
                    break
                if add%2==0:
                    add = add//2
                    p_add += 1
                if minus%2==0:
                    minus = minus//2
                    p_minus += 1
            if n == 3:
                step = step + 2
                break
            if p_add>p_minus:
                n = n + 1
                step = step + 1
            else:
                n = n - 1
                step = step + 1
    return step
