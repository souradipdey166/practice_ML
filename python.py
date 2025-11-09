def func(c,v):
    if v == 0:
        return 1
    else:
        return c * func(c, v - 1) 