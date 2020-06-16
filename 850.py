def noDiscrepencies(keyWord, dictWord, cipher):
    for i in range(len(keyWord)):
        if cipher.get(keyWord[i]) != dictWord[i]:
            if cipher.get(keyWord[i]) != '*':
                return False
            if dictWord[i] in cipher.values():
                return False

    return True

def patternMatches(word1, word2):
    if len(word1) != len(word2):
        return False
    mapping1 = {}
    mapping2 = {}

    for i in range(len(word1)):
        mapping1.setdefault(word1[i],word2[i])
        mapping2.setdefault(word2[i],word1[i])
        if(word1[i] != mapping2.get(word2[i]) or word2[i] != mapping1.get(word1[i])) :
            return False

    return True 

def lineMatches(plainwords, words, cipher):
    if len(words) != len(plainwords):
        return False
    for i in range(len(words)):
        if patternMatches(words[i], plainwords[i]):
            if noDiscrepencies(words[i],plainwords[i],cipher):
                for j in range(len(words[i])):
                    cipher[words[i][j]] = plainwords[i][j]
            else:
                return False
        else:
            return False
    
    return True

                


def decrypt(lines, plaintext,results):
    plainwords = plaintext.split(" ")
    #words.sort(key=len, reverse=True)
    matched = False
    for line in lines:
        cipher = {}
        cipher.setdefault(" ", " ")
        for i in range(ord('a'),ord('z')+1):
            cipher.setdefault(chr(i),'*')
        words = line.split()
        matched = matched or lineMatches(plainwords, words, cipher)
        if matched:
            break

    if matched:       
        for line in lines:

            toAdd = ""
            for c in line:
                d = cipher.get(c)
                if d == '*' or d == None:
                    results.append("No solution.")
                    break
                toAdd += d
            results.append(toAdd)
    else:
        results.append("No solution.")
    

def main():

    results = []
    plaintext = "the quick brown fox jumps over the lazy dog"
    cases = int(input())
    input()

    while cases > 0:  
        lines = []
        line = input()
        while bool(line):
            lines.append(line)
            try:
                line = input()
            except:
                break
        decrypt(lines, plaintext,results)
        results.append("")
        cases -= 1
    results.pop()
    for r in results:
        print(r)
    return 0


if __name__ == '__main__':
    main()