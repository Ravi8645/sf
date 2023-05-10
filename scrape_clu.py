import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


url = 'https://www.everydayhealth.com/drugs/'
medicines = ['medicine1', 'medicine2', 'medicine3', 'medicine4']
reviews = []

for medicine in medicines:
    medicine_url = url + medicine + '/reviews'
    response = requests.get(medicine_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    reviews_div = soup.find('div', {'class': 'reviews_list_content'})
    reviews_list = reviews_div.find_all('div', {'class': 'reviews_listitemcontent_text'})
    reviews.extend([review.text for review in reviews_list])



df = pd.DataFrame({'reviews': reviews})


tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(df['reviews'])


kmeans = KMeans(n_clusters=2, random_state=42)
y_pred = kmeans.fit_predict(X)


score = silhouette_score(X, y_pred)
print('Silhouette Score:', score)


import math
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from clustream import CluStream

# Step 1: Scrape the data
url = 'https://www.everydayhealth.com/drugs/'
medicines = ['medicine1', 'medicine2', 'medicine3', 'medicine4']
reviews = []

for medicine in medicines:
    medicine_url = url + medicine + '/reviews'
    response = requests.get(medicine_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    reviews_div = soup.find('div', {'class': 'reviews_list_content'})
    reviews_list = reviews_div.find_all('div', {'class': 'reviews_listitemcontent_text'})
    reviews.extend([review.text for review in reviews_list])

# Step 2: Create a dataframe
df = pd.DataFrame({'reviews': reviews})

# Step 3: Preprocess the data
tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(df['reviews'])

# Step 4: Define the CluStream parameters
num_micro_clusters = 10
window_size = 100
time_decay = 0.9

# Step 5: Initialize the CluStream algorithm
clustream = CluStream(n_micro_clusters=num_micro_clusters, window_size=window_size, time_decay=time_decay)

# Step 6: Update the micro-clusters as new data arrives
for i in range(len(X)):
    data_point = X[i].toarray()[0]
    clustream.update(data_point)

# Step 7: Get the final clusters
labels = clustream.get_labels()
centroids = clustream.get_centroids()

# Step 8: Evaluate the results
score = silhouette_score(X, labels)
print('Silhouette Score:', score)
