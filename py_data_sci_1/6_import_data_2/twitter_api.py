import tweepy, json

consumer_key = "aVuh25Vk9xjyMXriXzJqWh6zD"
consumer_secret = "P7XfmFZrAI1LC1l2a5Kf8gmmyjFLzKE8FA3fgFCbH4Nsg5fX31"
access_token = "397021453-syG0JBnwdqvbMfmkYD4OBJ0rSpUPkQjwdm3nFiqz"
access_token_secret = "i7v6i1fsOVzycxQh39Yrq0DG8dhuifjAYR4EU6wStjcPk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#write listener class
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("data/tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)


#create Streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth, l)

#The line filters Twitter Streams to capture data by keywords:
#stream.filter(track=['clemson', 'alabama'])
stream.filter(track=['Jenner'])





