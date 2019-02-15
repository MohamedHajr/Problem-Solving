def minimumBribes(q):
    if len(q) < 2:
        return 0
    else :
        bribes = q[0] - q[1]
        if bribes > 2:
            return 'Too chaotic'
        elif bribes < 0:
            return minimumBribes(q[1:])
        else: 
            return bribes + minimumBribes(q[1:])

print(minimumBribes([2,5,1,3,4]))
