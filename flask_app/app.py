def workout(name, bodypart, budget, times, loc):

    loc = loc.lower()
    if loc == 'indoors':
        outdoors = False
    else : 
        outdoors = True

    events = [] # Format: Sublists containing [Name, Outdoors, Bodypart, Cost, Timing]

    events = {
        1: ['Mum', False , 'L', 69, 'E'],
        2: ['Dad', True, 'L', 420, 'E'],
        69: ['Dad', True, 'C', 1, 'M'],
        21: ['L', True, 'U', 420, 'M'],
        0: ['Dad', True, 'C', 4200, 'A'],
    }

    bias = {

    }


    for eventkey in events:
        currentbias = 0
        if events[eventkey][1] == outdoors:
            currentbias += 1
        if events[eventkey][2] == bodypart:
            currentbias += 1
        if events[eventkey][3] <= budget:
            currentbias += 1
        if events[eventkey][4] == times:
            currentbias += 1
        bias[eventkey] = currentbias

    bias = dict(sorted(bias.items(), key=lambda item: item[1], reverse=True))

    top3keys = []
    count = 0
    for biasitem in bias:
        top3keys.append(biasitem)
        count += 1
        if count == 3:
            break

    top3events = []
    for top3key in top3keys:
        top3events.append(events[top3key])

    return top3events
