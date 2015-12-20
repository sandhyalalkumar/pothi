from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='RdhuMu2XR0UyzE070GqP4HuUD'
consumer_key_secret = 'RI6IyqmEjHnypiJwmAop4vESMOPKIRL9mIKqe89Gp05QsbUW3N'


class listener(StreamListener):

	def on_data(self, data):
		print data
		return True


	def on_error(self, status):
		print status


auth =  OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

