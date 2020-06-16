import time

def noDiscrepencies(keyWord, dictWord, cipher):
    for i in range(len(keyWord)):
        if cipher.get(keyWord[i]) != dictWord[i]:
            if cipher.get(keyWord[i]) != '*':
                return False
            if dictWord[i] in cipher.values():
                return False

    return True


def setWord(cipher,dictionary,word,words,index,keys):
    toReplace = words[index]
    newKeys = set()
    for i in range(len(word)):
        if toReplace[i] not in keys:
            newKeys.add(toReplace[i])
        cipher[toReplace[i]] = word[i]
    if(index >= (len(words) - 1)) :
        return True
    nextWord = words[index + 1]

    for potentialMatch in dictionary:
        if patternMatches(nextWord, potentialMatch) :
            if noDiscrepencies(nextWord,potentialMatch,cipher) :
                if setWord(cipher,dictionary,potentialMatch,words,index + 1, keys | newKeys) :
                    return True

    for i in newKeys:
        cipher[i] = '*'
    return False

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


def decrypt(line, dictionary):
    words = line.split(" ")
    words.sort(key=len, reverse=True)
    cipher = {}
    cipher.setdefault(" ", " ")
    for i in range(ord('a'),ord('z')+1):
        cipher.setdefault(chr(i),'*')
    for word in dictionary:
        keys = set()
        if patternMatches(word,words[0]):
           if setWord(cipher,dictionary,word,words,0,keys):
               break
            
    result = ""

    for i in range(len(line)):
        result += cipher.get(line[i])
    return result
    

def main():

    results = []
    words = int(input())
    dictionary = [] 
    #total = 0
    while words > 0:
        dictionary.append(input())
        words -= 1
    while True:
        try:
            #t0 = time.clock()
            line = input()
            results.append(decrypt(line, dictionary))
            #t1 = time.clock()
            #print(f"{t1 - t0} seconds")
            #total += (t1 - t0)
        except:
            break
    
    for r in results:
        print(r)
    #print(f"total time: {total}")

if __name__ == '__main__':
    main()
