import time
import pandas as pd 
from ntscraper import Nitter
scraper = Nitter()
# assumption that a single tweet can include the stock multiple times that's why I splitted the tweet on the stock in an array where stock will be repeated the size of the array-1
def fetch_tweets_for_user(usernames,stock):
    global count
    for username in usernames:
      base_url = 'https://twitter.com/'
      username = username.replace(base_url, '')  
      tweets_data = scraper.get_tweets(username, mode='user')
      final_tweets = [tweet['text'] for tweet in tweets_data['tweets']]
      for tweet in final_tweets:
          if stock in tweet:
             arr=tweet.split(stock)
             count += len(arr)-1
    return count

if __name__ == "__main__":
    stock = "$TSLA" # specify here the stock you want to search for 
    accounts = [
        "https://twitter.com/Mr_Derivatives", 
        "https://twitter.com/warrior_0719",
        "https://twitter.com/ChartingProdigy",
         "https://twitter.com/RoyLMattox"
        # ,"https://twitter.com/allstarcharts",
        # "https://twitter.com/yuriymatso",
        # "https://twitter.com/TriggerTrades", 
        # "https://twitter.com/AdamMancini4", 
        # "https://twitter.com/CordovaTrades",
        # "https://twitter.com/Barchart"
    ]  # specify here the usernames 
    minutes = 1 #specify here the time interval 
    total_minutes = 0
    interval = minutes * 60
    while True:
            count = 0 # number of times the stock is repeated
            fetch_tweets_for_user(accounts, stock)
            total_minutes += minutes #after every total-minutes we have this print statement
            print(f"{stock} was mentioned {count} times in the last {total_minutes} minutes")
            time.sleep(interval)
#Ater running the following commands through the shell:
# pip install ntscraper
# pip install tqdm
# the above code can be executed

   