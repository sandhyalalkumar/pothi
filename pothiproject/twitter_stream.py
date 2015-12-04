from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'PEBSALWRo5SsRKTH2nLVi5hWi'
csecret = '0cmd5RVjHXaFMyKtWtP1AXlML218Ru0oID6tcxfA0il5t51Zjz'
atoken = '3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr'
asecret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'


class listener(StreamListener):

	def on_data(self, data):
		print data
		return True


	def on_error(self, status):
		print status


auth =  OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Car"])

