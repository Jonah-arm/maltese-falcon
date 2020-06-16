def find_losers(current_votes):
    losers = []
    min = current_votes[0]
    for x in range(len(current_votes)):
        if( current_votes[x] < min):
            min = current_votes[x]
            losers = []
            losers.append(x)
        elif current_votes[x] == min:
            losers.append(x)
    return losers


def get_winners(ballots, candidates):
    winners = []
    win_requirement = len(ballots) / 2 + 1
    current_candidates = candidates[:]
    
    while len(winners) == 0:
       # input()
        current_votes = []
        for y in current_candidates:
            current_votes.append(0)
      #  print("")
      #  print("Votes:")
        for x in ballots:
       #     print("index: {}".format(x[0] - 1))
       #     print(candidates[x[0] - 1])
            current_votes[current_candidates.index(candidates[x[0] - 1])] += 1
       # print("")
        for z in current_votes:
            if z >= win_requirement:
                return [current_candidates[current_votes.index(z)]]
        losers = find_losers(current_votes)
        if len(losers) == len(current_candidates):
            result = []
            for c in current_candidates:
                result.append(c)
            return result
       # print("")
       # print("Initial Ballot")
       # for x in ballots:
       #     print(x)
        for x in ballots:
            for index in losers:
                x.remove(candidates.index(current_candidates[index]) + 1)
        temp_candidates = current_candidates[:]
       # print("")
      #  print("To Remove:")
        for index in losers:
       #     print("index: {}".format(candidates.index(current_candidates[index])))
       #     print(current_candidates[index])
            temp_candidates.remove(current_candidates[index])
        current_candidates = temp_candidates
       # print("")
       # print("Post-removal Ballot")
       # for x in ballots:
        #    print(x)  
    

def main():
    line = input()
    cases = int(line)
    input()
    while cases > 0:
        line = input()
        n = int(line)
        candidates = []
        for x in range(n):
            candidates.append(input())

        ballots = []
        line = input()
        while bool(line):
            ballot = []
            line = line.split()
            for i in line:
                ballot.append(int(i))

            ballots.append(ballot)
            line = input()
        winners = get_winners(ballots, candidates)
        for to_print in winners:
            print(to_print)
        if cases > 1:
            print("")

        cases -= 1

if __name__ == '__main__':
    main()

