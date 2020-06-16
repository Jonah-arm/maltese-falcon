def isJolly(nums):
    n = int(nums[0])
    if(n == 1):
        return True
    i = 1
    curr = int(nums[1])
    jollies = set()
    while i <= n :
        prev = curr
        curr = int(nums[i])
        diff = abs(prev - curr)
        if(diff >= n or diff in jollies):
            return False
        jollies.add(diff)
        i += 1
    return True


def main():
    results = []
    while True:
        try:
            line = input()
            nums = line.split(" ")
            results.append(isJolly(nums))
        except:
            break
    
    for r in results:
        if(r):
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == '__main__':
    main()
