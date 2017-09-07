import pandas as pd 
import json
import sys

file_name = 'data/tweets.txt'

# intiialize empty list
tweets_list = list()

with open(file_name, 'r') as tweets_file:
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_list.append(tweet)

# tweets_list is a list of dicts
print(tweets_list[0].keys())
print(tweets_list[0]['text'])

counts = dict()

for i, item in enumerate(tweets_list):
    words = item['text'].split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

word_list = list()

for key, val in counts.items():
    word_list.append( (val, key) )

word_list.sort(reverse=True)

for val, key in word_list:
    print(key, val)


