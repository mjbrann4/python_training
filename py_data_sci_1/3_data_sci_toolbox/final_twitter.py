# Select retweets from the Twitter dataframe: result
result = filter(lambda x: x[0:2]=='RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)



# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    try:
        col = df[col_name]
        
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] = 1
        return cols_count

    except:
        print('The dataframe does not have a ' + col_name + ' column.')

result1 = count_entries(tweets_df, 'lang')
print(result1)
result2 = count_entries(tweets_df, 'lang1')


