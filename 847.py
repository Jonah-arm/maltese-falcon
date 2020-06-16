
dp = {}

def whoWins(p,i,n,turn):
    if(p*i >= n):
        dp.setdefault(p*i,True)
        return turn
    if(p*i in dp):
        if dp[p*i]:
            return turn
        return not turn
    for j in range(2,10):
        if whoWins(p*i,j,n, not turn) != turn:
            dp.setdefault(p*i, False)
            return not turn
    dp.setdefault(p*i,True)
    return turn 

def main():
    results = []
    while True:
        try:
            dp.clear()
            p = 1
            n = int(input())
            #False is Ollie's turn, True is Stan's.
            turn = True
            results.append(False)

            for i in range(2,10):
                if whoWins(p,i,n,turn):
                    results[-1] = True
                    break
        except:
            break
    
    for r in results:
        if(r):
            print("Stan wins.")
        else:
            print("Ollie wins.")

if __name__ == '__main__':
    main()
