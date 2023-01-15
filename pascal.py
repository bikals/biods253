
def pascal():
    pas = []
    j = 1

    while j < 11:
        for i in range(j):
            if i == 0:
                pas.append(1)
                i += 1
                continue
            if i == j-1:
                pas.append(1)
                break
            pas.append(pas[len(pas) - j] + pas[len(pas) - (j-1)])
        j += 1

    n = 1
    m = 0
    while n < 11:
        for i in range(n):
            if i + m > len(pas) - 1:
                break
            if i == n-1:
                print(pas[i + m])
            else:
                print(pas[i + m], end=' ')
        m += n
        n += 1

pascal()

