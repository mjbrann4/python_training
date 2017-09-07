#dictionaries are very efficient to look up values

#keys are unique and immutable
world = {"afghanistan": 30.55, "albania": 2.77, "algeria": 39.21}
print(world["albania"])

#use keys() method to determine which keys available
print(world.keys())

#cannot use lists as dict keys

#add to dict
world["mexico"] = 40.43
print(world)

#verify a key exists
print('mexico' in world)

#remove an item from dict
del(world['mexico'])
print(world)


#if you have a collection of values where order matters use a list
#if you need a lookup table with unique keys use a dict


#dicts within dicts is fine
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)