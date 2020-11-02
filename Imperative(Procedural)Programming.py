def increment(n):
    return n+1

def square(n):
    return n**2

def findSequence(initial, goal):
    candidates = [(str(initial), initial)]
    
    for i in range (1, goal - initial + 1):
        newCandidates = []
       
        for (action, result) in candidates:
            # ENABLE WHILE DEBUGGING:
            # print("Candidates",i,":",candidates)
            # print("Action: ",action,"Result: ",result)
            
            for (a,r) in [(" increment ", increment), (" square ", square)]:
                newCandidates.append((action + a, r(result)))
                print (i, ": ", newCandidates[-1])
                
                if newCandidates[-1][1] == goal:
                    return newCandidates[-1]
        candidates = newCandidates

# EXAMPLE
answer = findSequence(1, 10)
print("Shortest path is:",answer)
