import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


data = pd.read_csv("./file2.csv", encoding="latin1")


stop_words = ['subject:','i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
      'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 
      'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 
      'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 
      'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 
      'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 
      'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 
      'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 
      'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 
      'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 
      'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', 
      '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


"""
def remove_filter_words(text):
	
	if type(text) != str:
		raise TypeErrorß
	
	#text = str(text)

	words = text.lower().split()

	filtered_words = [w for w in words if not w in stop_words and len(w) > 4]

	new = " ".join(filtered_words)

	return new

data['text'] = data.text.apply(remove_filter_words)
"""

data['text'] = data.text.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))



"""
print(data["spam"].value_counts())

0    4361
1    1496
Name: spam, dtype: int64

P(h) = 1 - 1496/4361 = 0.6569594129786747
P(s) = 1496/4361 = 0.34304058702132534
"""


train, test = train_test_split(data, test_size=0.3, random_state=42)

