##The code I used to get the twitter data.

# About twitterstream.py: Used to fetch live stream data from twitter. Requires oauth2, which is not part of the EnThought Python library. usage: Open the program and replace access_token_key, access_token_secret, consumer_key, and consumer_secret with the appropriate values. Then run $ python twitterstream.py To get credentials:

# Create a twitter account if you do not already have one.
# Go to https://dev.twitter.com/apps and log in with your twitter credentials.

# Click "create an application"

# Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.

# On the next page, scroll down and click "Create my access token"
# Copy your "Consumer key" and your "Consumer secret" into twitterstream.py

# Click "Create my access token." You can Read more about Oauth authorization.

# Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret
# Run the following and make sure you see data flowing.

# $ python twitterstream.py

# When you're ready to create your dataset, go ahead and run:

# $ python twitterstream.py > output.txt

# But don't let the script run for too long. I generated my dataset by letting
# the script run for 10 minutes.


import oauth2 as oauth
import urllib2 as urllib

# See Assignment 1 instructions or README for how to get these credentials.
access_token_key = "YOUR KEY HERE"
access_token_secret = "YOUR SECRET HERE"

consumer_key = "YOUR KEY HERE"
consumer_secret = "YOUR SECRET HERE"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

if __name__ == '__main__':
  fetchsamples()
