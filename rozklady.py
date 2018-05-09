def jednostajny(n):
    x=[1/n]*n
    return x
def harmoniczny(n):
    x=[None]*n
    h = 0
    for j in range(n+1):
        if j > 0:
            h += 1 / j
    for i in range(n+1):
        if i>0:
            #print(h)
            x[i-1]=1/(i*h)
    return x

def dwuharmoniczny(n):
    x=[None]*n
    h=0
    for j in range(n+1):
        if j > 0:
            h += 1 / (j**2)
    for i in range(n+1):
        if i>0:
            #print(h)
            x[i-1]=1/((i**2)*h)
    return x

def geometryczny(n):
    x=[None]*n
    for i in range(n+1):
        if i>0:
            if i ==n:
                x[i-1]=1/(2**(n-1))
            else:
                x[i-1]=1/(2**i)

    return x
