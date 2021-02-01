def fact(x):
    if x == 1:
        return(1)
    else:
        n = x * fact(x - 1)
    return(n)
