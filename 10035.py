"""
def getOps(n1, n2):
    i = len(n1) - 1
    j = len(n2) - 1
    carries = 0
    cary = 0


    while i >= 0 and j >= 0:
        num = int(n1[i]) + int(n2[j])
        if cary > 0:
            num += 1
            cary = 0
        if num >= 10:
            cary = 1
            carries += 1
        i -= 1
        j -= 1
    while i >= 0 and cary > 0:
        num = int(n1[i]) + cary
        cary = 0
        if num  >= 10:
            cary = 1
            carries += 1
        i -= 1

    while j >= 0 and cary > 0:
        num = int(n2[j]) + cary
        cary = 0
        if num  >= 10:
            cary = 1
            carries += 1
        j -= 1
    
    return carries

def main():
    nums = input().split()
    n1 = nums[0]
    n2 = nums[1]

    while int(n1) != 0 and int(n2) != 0 :
        ops = getOps(n1, n2)
        if ops == 0:
            print('No carry operation.')
        elif ops == 1:
            print(f'{ops} carry operation.')
        else: 
            print(f'{ops} carry operations.')
        nums = input().split()
        n1 = nums[0]
        n2 = nums[1]

if __name__ == '__main__':
    main()
"""
def getOps(n1, n2):
    i = len(n1) - 1
    j = len(n2) - 1
    carries = 0
    cary = 0


    while i >= 0 and j >= 0:
        num = int(n1[i]) + int(n2[j])
        if cary > 0:
            num += 1
            cary = 0
        if num >= 10:
            cary = 1
            carries += 1
        i -= 1
        j -= 1
    while i >= 0 and cary > 0:
        num = int(n1[i]) + cary
        cary = 0
        if num  >= 10:
            cary = 1
            carries += 1
        i -= 1

    while j >= 0 and cary > 0:
        num = int(n2[j]) + cary
        cary = 0
        if num  >= 10:
            cary = 1
            carries += 1
        j -= 1
    
    return carries

def main():
    nums = input().split()
    n1 = nums[0]
    n2 = nums[1]
    results = []

    while int(n1) != 0 or int(n2) != 0 :
        ops = getOps(n1, n2)
        if ops == 0:
            #print('No carry operation.')
            results.append('No carry operation.')
        elif ops == 1:
            #print(f'{ops} carry operation.')
            results.append(f'{ops} carry operation.')
        else: 
            #print(f'{ops} carry operations.')
            results.append(f'{ops} carry operations.')
        nums = input().split()
        n1 = nums[0]
        n2 = nums[1]
    
    for line in results:
        print(line)

if __name__ == '__main__':
    main()
