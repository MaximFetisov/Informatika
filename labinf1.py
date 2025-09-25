def simss(a):
    n = 7
    m = 0
    an = []
    anc = []

    if a < 0:
        a = -1 * a
        m = 1
    while a != 0:
        an.append(a%7)
        a = a // 7
    an += [0]
    
    for i in range(len(an)-1):
        if an[i] > 7/2:
            an[i] -= 7
            an[i+1] += 1

    if m == 0:
        for i in range(len(an)-1,-1,-1):
            anc.append(an[i])
    else:
        for i in range(len(an)-1,-1,-1):
            anc.append(-1*an[i])
    return anc

a = int(input())

if simss(a)[0] == 0 and len(simss(a)) > 1:
    print(*simss(a)[1:])
else:
    print(*simss(a))