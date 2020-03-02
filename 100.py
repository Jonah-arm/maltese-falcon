import sys

def getAnswer(i, j):
    m = 0
    for n in range(i, j+1):
        k = 1
        while n != 1:
            if n % 2 == 1:
                n = 3 * n + 1
                k += 1
            else:
                n = n / 2
                k += 1
        if k > m:
            m = k
    return m


for l in sys.stdin:
    if  len(l) == 0:
        break
    line = l.split()
    i = int(line[0])
    j = int(line[1])
    k = getAnswer(i,j)
    print(i, j, k)
    l = input()

