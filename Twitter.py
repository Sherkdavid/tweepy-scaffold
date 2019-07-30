import tweepy

def main():
    # http://docs.tweepy.org/en/v3.5.0/api.html
    # Login Account
    auth = tweepy.auth.OAuthHandler("Your Consumer Key", "Your Consumer Secret")

    # Validate application with dev tokens
    auth.set_access_token("Your Dev Key", "Your Dev Secret")
    api = tweepy.API(auth)

    # Get Timeline
    consumer_timeline = api.home_timeline()