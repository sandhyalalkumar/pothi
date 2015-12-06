import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import json, io

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='BdSJ15kEkzUPep0fL03akBryN'
consumer_key_secret = 'Rl6qRcfEd2XAiaZy0a0lQSHpEWxMaiwqIbJCvuoUO2HglXXi6f'

start_time = time.time()
keyword_list = ['Ajinkya Rahane',]

class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, data):
		counter = 5
		while True:
		#while(counter > 0):

			try:
				self.tweet_data.append(data)

				with open('large_on_Ajinkya_rahane_tweets.json', 'a') as outfile:
					outfile.write(data)

				print(data)
				print(type(data))
				print ""
				#counter = counter - 1
				print(time.time() - self.time)
				if (time.time() - self.time) > self.limit:
					print "Your time up, no anymore data"
					break
				return True

			except BaseException, e:
				print 'Failed on data, ', str(e)

		print "New thing Started"

		exit()

	def on_error(self, status):
		print status

if __name__ == '__main__':

	listenObj = listener(start_time,12000)
	authrize = OAuthHandler(consumer_key, consumer_key_secret)
	authrize.set_access_token(access_token, access_token_secret)
	new_stream = Stream(authrize,listenObj)

	#new_stream.filter(track=['python', 'javascript', 'ruby']) 
	new_stream.filter(track=keyword_list)
	time.sleep(2)
	