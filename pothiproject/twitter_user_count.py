import json
from pprint import pprint 
import ast
import pandas as pd

def user_count(file_name):

	with open(file_name, 'r') as handle:
		json_data = [json.loads(line) for line in handle]

	user_tweets_count = {}
	for jdata in json_data:
		#print(type(json_data[0]))
		#print(jdata['user']['screen_name'])
		#print(len(json_data))
		k = jdata['user']['screen_name']
		if k not in user_tweets_count:
			user_tweets_count[k] = 1
		else:
			c = user_tweets_count[k]
			c = c + 1
			user_tweets_count[k] = c
	#print(user_tweets_count)

	print(len(user_tweets_count))
	df = pd.DataFrame(user_tweets_count.items(), columns=['user', 'tweet_count'])
	print df
	#for key in user_tweets_count:
	#	print key, user_tweets_count[key]



if __name__ == '__main__':
	user_count('large_on_Ajinkya_rahane_tweets.json')