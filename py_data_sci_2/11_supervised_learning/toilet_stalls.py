import numpy as np
import collections

np.random.seed(123)

toilet_trials = []
tries = []

# simulate 10000 occurances of toilet stalls 
# PR(both empty) = 1/3
# PR(both taken) = 1/3
# PR(one taken) = 1/3

for i in range(10000):
    random1 = np.random.uniform(0,1)
    random2 = np.random.uniform(0,1)
    if random1 <= (1/3):
        toilet_trials.append( (0,0) )
    elif random1 <= (2/3):
        toilet_trials.append( (1,1) )
    else:
        #if one taken, then equal chance of first or second one taken
        if random2 <= .5:
            toilet_trials.append( (0,1) )
        else:
            toilet_trials.append( (1,0) )

# probability of opening door 1 and it is empty = 0.5
trial_collection = collections.Counter(toilet_trials)
print('Collection of toilet trials:', trial_collection)

# loop over toilet trials and find probability second stall is taken- given first stall is empty
for i, val in enumerate(toilet_trials):
    if val[0] == 0:
        if val[1] == 0:
            tries.append(0)
        else:
            tries.append(1)

print('Probability of second stall taken, given first empty:', np.mean(tries))

