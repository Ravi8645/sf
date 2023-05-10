import pandas as pd
import numpy as np

import snscrape.modules.twitter as sntwitter

query = "(@UmdarTamker)"
tweets = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i>10:
        break
    else:
        print(tweet.rawContent)
        # print(str(tweet.date).split()[1].split('+')[0])

