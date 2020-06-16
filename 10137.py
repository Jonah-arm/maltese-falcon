def average(cost):
    total = 0.0
    for x in cost:
        total += x

    return total / round(float(len(cost)),2)

def getOutput(cost):
    average_cost = average(cost)
    debit = 0.0
    credit = 0.0

    for x in cost:
        if x > average_cost:
            debit = round(debit + ( x - average_cost),2)
        elif x < average_cost:
            credit = round(credit + (average_cost - x),2)

    return min(credit, debit)

def main():
    line = input()
    n = int(line)

    while n!= 0 :
        cost = []
        for x in range(n):
            cost.append(float(input())) 
        
        print("$%.2f" % getOutput(cost))
        line = input()
        n = int(line)

if __name__ == '__main__':
    main()

