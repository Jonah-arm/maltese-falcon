import sys
cache = {}

def length(n):
    if n in cache:
        return cache[n]
    if n == 1:
        return 1
    orgin = n
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3*n + 1
    count = length(n) + 1
    cache[orgin] = count
    return count

def getAnswer(i, j):
    m = 0
    for n in range(i, j + 1):   
        k = length(n)
        if k > m:
            m = k
    return m

def main():
    for line in sys.stdin:
        if not line:
            break
        i, j = [int(x) for x in line.split()]
        if i > j:
            start_point = j
            end_point = i
        else:
            start_point = i
            end_point = j
        maxlength = getAnswer(start_point, end_point)
        print(i, j, maxlength)

if __name__ == '__main__':
    main()

