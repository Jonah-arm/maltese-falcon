import sys
cache = {}

def getAnswer(i, j):
    m = 0
    for n in range(i, j+1):
        initial = n
        if(n in cache):
            k = cache[n]
        else:   
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
        cache[initial] = k
    return m

def main():
    for line in sys.stdin:
        if not line:
            break
        i, j = [int(x) for x in line.split()]
        if i > j:
            i, j = (j, i)
        maxlength = getAnswer(i, j)
        print(i, j, maxlength)

if __name__ == '__main__':
    main()