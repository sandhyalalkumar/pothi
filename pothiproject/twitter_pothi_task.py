import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import json, io
import sys
import pandas as pd

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='BdSJ15kEkzUPep0fL03akBryN'
consumer_key_secret = 'Rl6qRcfEd2XAiaZy0a0lQSHpEWxMaiwqIbJCvuoUO2HglXXi6f'


class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, data):
		while True:
			try:
				self.tweet_data.append(data)

				#with open('car_bmw.json', 'w') as outfile:
				#	outfile.write(data)

				#print(data)
				#print(type(data))
				#print " "
				#print(time.time() - self.time)
				if (time.time() - self.time) > self.limit:
					print "*************************************"
					print "Time completed, Please get the result"
					print "*************************************"
					break
				return True

			except BaseException, e:
				print 'Failed on data, ', str(e)
		#print "New thing Started"
		user_tweets_count={}
		for jdata in self.tweet_data:
			d = json.loads(jdata)
			k = str(d['user']['screen_name'])
			if k not in user_tweets_count:
				user_tweets_count[k] = 1
			else:
				c = user_tweets_count[k]
				c = c + 1
				user_tweets_count[k] = c

		print "Total no of tweets taken : %d"%(len(user_tweets_count))
		#print user_tweets_count
		df = pd.DataFrame(user_tweets_count.items(), columns=['user', 'tweet_count'])
		#print df
		df.to_csv("twitter_user_count.csv")
		exit()

	def on_error(self, status):
		print status

if __name__ == '__main__':
	tim = raw_input( "Enter time in minutes:")
	n = raw_input("No of Keywords:")
	n1 = int(n)
	keywords_list = []
	while(n1 > 0):
		keywords_list.append(raw_input("Enter a keyword:"))
		n1 = n1 - 1

	print "************************************"
	print "Please wait for %d minutes"%int(tim)
	print "************************************"

	start_time = time.time()
	listenObj = listener(start_time,60*int(tim))
	authrize = OAuthHandler(consumer_key, consumer_key_secret)
	authrize.set_access_token(access_token, access_token_secret)
	new_stream = Stream(authrize,listenObj)
	new_stream.filter(track=keywords_list)

	