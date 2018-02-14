def answer(n): 
    prime = [2]
    p_str = "2"
    for x in range(3,50000):
        not_prime = False
        for y in prime:
            if x%y==0:
                not_prime = True
                break
        if not not_prime:
            prime.append(x)
            p_str += str(x)
            if len(p_str)>(n+5):
                return str(p_str[n:n+5])
