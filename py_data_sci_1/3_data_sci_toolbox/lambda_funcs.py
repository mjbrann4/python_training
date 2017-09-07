
#lambda allow quick and dirty function writing
#list arguments, colon, what we want to return
raise_to_power = lambda x, y: x ** y
print(raise_to_power(2, 3))


#map function takes a function and a sequence and applies function over
#all elements in the sequence

#can pass lambda functions to map without naming- anonymous functions
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)

#this is a map object
print(square_all)
print(list(square_all))

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1*echo)
# Call echo_word: result
result = echo_word('hey', 5)
# Print result
print(result)


# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]
# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)
# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
# Convert shout_spells into a list and print it
print(shout_spells_list)

