def answer5(start, length):
    result = 0
    if start%2==0:
        for x in range(length, 0, -1):
            if x%4==1:
                result ^= (start+length*(length-x+1)-(length-x+1))
            elif x%4==2:
                if length%2==1:
                    result ^= (start+length*(length-x+1)-(length-x+1))^(start+length*(length-x))
                else:
                    result ^= 1
            elif x%4==3:
                result ^= (start+length*(length-x+1)-(length-x+1))^1
            else:
                if length%2==1:
                    result ^= (start+length*(length-x+1)-(length-x+1))^(start+length*(length-x))^1
                                  
    else:
        for x in range(length, 0, -1):
            if x%4==1:
                result ^= (start+length*(length-x))
            elif x%4==2:
                if length%2==0:
                    result ^= (start+length*(length-x+1)-(length-x+1))^(start+length*(length-x))
                else:
                    result ^= 1
            elif x%4==3:
                result ^= (start+length*(length-x))^1
            else:
                if length%2==0:
                    result ^= (start+length*(length-x+1)-(length-x+1))^(start+length*(length-x))^1
    return result
