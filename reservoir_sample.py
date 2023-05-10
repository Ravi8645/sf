import random as rd
import re
import math
import string

def pre_process_tweets(url):

    f = open(url, "r", encoding="utf8")
    tweets = list(f)
    list_of_tweets = []

    for i in range(len(tweets)):

        # remove \n from the end after every sentence
        tweets[i] = tweets[i].strip('\n')

        # Remove the tweet id and timestamp
        tweets[i] = tweets[i][50:]

        # Remove any word that starts with the symbol @
        tweets[i] = " ".join(filter(lambda x: x[0] != '@', tweets[i].split()))

        # Remove any URL
        tweets[i] = re.sub(r"http\S+", "", tweets[i])
        tweets[i] = re.sub(r"www\S+", "", tweets[i])

        # remove colons from the end of the sentences (if any) after removing url
        tweets[i] = tweets[i].strip()
        tweet_len = len(tweets[i])
        if tweet_len > 0:
            if tweets[i][len(tweets[i]) - 1] == ':':
                tweets[i] = tweets[i][:len(tweets[i]) - 1]

        # Remove any hash-tags symbols
        tweets[i] = tweets[i].replace('#', '')

        # Convert every word to lowercase
        tweets[i] = tweets[i].lower()

        # remove punctuations
        tweets[i] = tweets[i].translate(str.maketrans('', '', string.punctuation))

        # trim extra spaces
        tweets[i] = " ".join(tweets[i].split())

        # convert each tweet from string type to as list<string> using " " as a delimiter
        list_of_tweets.append(tweets[i].split(' '))

    f.close()

    return list_of_tweets



def reservoir_sampling(data, n): 
    sample_data = []
    for i, x in enumerate(data):
        if i < n:
            sample_data.append(x)
        else:
            m = rd.randint(0, i)
            if m < n:
                sample_data[m] = x
    return sample_data
if __name__ == '__main__':

    data_url = 'cnnhealth.txt'

    tweets = pre_process_tweets(data_url)

    # default number of experiments to be performed
    experiments = 5

    # default value of K for K-means
    k = 5

    # for every experiment 'e', run K-means
    for e in range(experiments):
        print("------ Running reserviour sampling  for experiment no. " + str((e + 1)) + " for size = " + str(k))
        s=reservoir_sampling(tweets, k)
        print(s)
        print("\n")
