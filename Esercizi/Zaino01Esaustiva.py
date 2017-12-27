def FractionalKnapsak(v,p,P):
    current_p = P

    b = []

    for i in range(len(v)):
        b.append(v[i]/p[i])

    i = 0
    value = 0

    while current_p > 0 and i < len(v):
        pi = min(current_p,p[i])
        value += pi * b[i]
        current_p -= pi
        i += 1

    return value

def prodottoScalare(x,v,t):
    sum = 0
    for i in range(t):
        sum += x[i] * v[i]
    return sum

def zaino01esaustiva(v,p,k,P,x,solution=0):
    if k >= len(v):
        sum = prodottoScalare(x,v,len(v))
        if sum > solution:
            print(sum)
            solution = sum
    else:
        bound = prodottoScalare(x,v,k-1) + FractionalKnapsak(v[k:],p[k:],P)
        if bound > solution:
            xc = x.copy()
            xc[k] = 0
            zaino01esaustiva(v,p,k+1,P,xc,solution)
            if P - p[k] >= 0:
                xc1 = x.copy()
                xc1[k] = 1
                zaino01esaustiva(v, p, k + 1, P - p[k], xc1, solution)

p = [1,2,3,4]
v = [40,30,20,10]
P = 7
x = [0,0,0,0]

zaino01esaustiva(v,p,0,P,x)