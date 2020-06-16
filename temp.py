global answer, candidate_names, voters, candidate_votes, no_of_voters, count, mid, VOTERS

no_of_itterations = int(input("Enter no of itterations : "))

def Match_candidate(x):
    global count, answer, voters, VOTERS
    
    per = 10**(no_of_candidates-1)
    y = x//per
    y-=1 #since user entered candidate from 1 not 0
    
    candidate_votes[y]+=1
    if(candidate_votes[y]>mid and answer==False):
        print(candidate_names[y])
        answer=True
        return
    else:
        count+=1

    if(count==no_of_voters):
        for i in range(0,no_of_candidates):
            for j in range(0,no_of_candidates):
                if(candidate_votes[i]<candidate_votes[j]):
                    min = i             #find minimum
        min+=1 
        #since user entered candidate from 1 not 0
        #cnt = 0
        VOTERS = []          #to change 'voters' list
        for x in voters:
            per = 10**(no_of_candidates-1)
            y = x//per
            #cnt+=1
            if(y==min):
                x = x%per
                x = x*10
            VOTERS.append(x)
                
        
            

while(no_of_itterations):
    no_of_candidates = int(input("Enter no of candidates : "))

    answer = False
    candidate_names = []
    voters = []                                
    candidate_votes = []
    no_of_voters = 0
    count=0
    

    for i in range(0,no_of_candidates):
        candidate_votes.append(int(0))

    print("\nEnter names : \n")
    for i in range(0,no_of_candidates):
        candidate_names.append(input())
        
    while(1):
        temp = input()
        if len(temp.strip()) == 0 :    #check empty line
            break
        else:
            voters.append(int(temp))
        no_of_voters+=1

    mid = no_of_voters/2
        
    while(answer==False):
        for i in voters:
            Match_candidate(i) 
            #calculate candidate votes and rearrenge while 
            #elliminating
            if(answer==True):
                break

        for i in range(0,no_of_candidates):
            candidate_votes[i] = 0
        count=0
        voters = VOTERS

    no_of_itterations-=1