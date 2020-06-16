 

def main():
    cases = int(input())

    results = []
    for x in range(cases):
        input()
        characters = []
        line = input().split(" ")
        m = int(line[0])
        n = int(line[1])
        for y in range(m):
            line = input()
            characters.append(list(line.lower()))
        k = int(input())
        words = []
        for l in range(k):
            words.append(input().lower())
        
        for word in words:
            found = False
            mMin = m
            nMin = n
            for i in range(m):
                for j in range(n - len(word) + 1):
                    k = 0
                    for c in word:
                        d = characters[i][j + k]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        mMin = i
                        nMin = j
                        found = True
                        break
                if found :
                    break

            found = False
            for i in range(m):
                for j in range(n - 1, len(word) - 2,-1):
                    k = 0
                    for c in word:
                        d = characters[i][j - k]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(i < mMin) :
                            mMin = i
                            nMin = j
                        elif i == mMin :
                            if j < nMin :
                                mMin = i
                                nMin = j

                        found = True
                        break
                if found :
                    break
        
            found = False
            for i in range(n):
                for j in range(m - len(word) + 1):
                    k = 0
                    for c in word:
                        d = characters[j + k][i]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(j < mMin) :
                            mMin = j
                            nMin = i
                        elif j == mMin :
                            if i < nMin :
                                mMin = j
                                nMin = i
                        found = True
                        break
                if found :
                    break

            found = False
            for i in range(n):
                for j in range(m - 1, len(word) - 2, -1):
                    k = 0
                    for c in word:
                        d = characters[j - k][i]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(j < mMin) :
                            mMin = j
                            nMin = i
                        elif j == mMin :
                            if i < nMin :
                                mMin = j
                                nMin = i
                        found = True
                        break
                if found :
                    break

            found = False
            for i in range(m - len(word) + 1):
                for j in range(n - len(word) + 1):
                    k = 0
                    for c in word:
                        d = characters[i + k][j + k]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(i < mMin) :
                            mMin = i
                            nMin = j
                        elif i == mMin :
                            if j < nMin :
                                mMin = i
                                nMin = j
                        found = True
                        break
                if found :
                    break

            found = False
            for i in range(m - 1, len(word) - 2, - 1):
                for j in range(n - 1, len(word) - 2, -1):
                    k = 0
                    for c in word:
                        d = characters[i - k][j - k]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(i < mMin) :
                            mMin = i
                            nMin = j
                        elif i == mMin :
                            if j < nMin :
                                mMin = i
                                nMin = j
                        found = True
                        break
                if found :
                    break

            found = False
            for i in range(m - len(word) + 1):
                for j in range(n - 1, len(word) - 2, -1):
                    k = 0
                    for c in word:
                        d = characters[i + k][j - k]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(i < mMin) :
                            mMin = i
                            nMin = j
                        elif i == mMin :
                            if j < nMin :
                                mMin = i
                                nMin = j
                        found = True
                        break
                if found :
                    break

            found = False
            for i in range(m - 1, len(word) - 2, -1):
                for j in range(n - len(word) + 1):
                    k = 0
                    for c in word:
                        d = characters[i - k][j + k]
                        if c != d :
                            break
                        k += 1
                    if k == len(word) :
                        if(i < mMin) :
                            mMin = i
                            nMin = j
                        elif i == mMin :
                            if j < nMin :
                                mMin = i
                                nMin = j
                        found = True
                        break
                if found :
                    break

            results.append(f"{mMin + 1} {nMin + 1}")
        results.append(" ")
        
    for r in results:
        print(r)


if __name__ == '__main__':
    main()
