from twitter import *
import csv
from time import sleep

def extract_tweets(hashtags, filename):
    while True:
        print('starting')
        try:
            t = TwitterStream(auth=OAuth('926787882173464576-3RrisMX4YxbzNyqcLw4OUoj77xCocgi','5lFiwBGQ5aEBTTUtBMCFYbPQiEQg4oBVy4SfdOe9cBjmq',
                '2Lw1bOrqNTJ8NfLn4fPu21oV8', '1pG38Wme94nSxUI7SuLZD4yeBxZHBFkajyj6syPcRFuIvIk4sl'))
            msg = t.statuses.filter(track=hashtags, language='en')
            for i in msg:
                keys = i.keys()
                if 'id' in keys and 'text' in keys and 'created_at' in keys and 'user' in keys:
                    line = []
                    line.append(i['id'])
                    line.append(i['text'])
                    line.append(i['created_at'])
                    line.append(i['user']['id'])
                    with open(filename,'a',newline='') as fp:
                        writter = csv.writer(fp, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC)
                        writter.writerow(line)
        except Exception as e:
            print(e)
        print('sleeping')
        sleep(30)


extract_tweets('#ethereum,#ether,#eth', 'twitter_eth.csv')
