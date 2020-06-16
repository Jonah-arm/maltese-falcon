import math

def main():
    results = []
    n = int(input())
    while n != 0:
        root = int(math.sqrt(n))
        if root * root == n:
            results.append(True)
        else:
            results.append(False)
        n = int(input())
    
    for r in results:
        if(r):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    main()
