import pandas as pd
import numpy as np
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/stress.csv")
print(data.head())
print(data.isnull().sum())
import nltk
import re
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopwords=set(stopwords.words("english"))
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*/\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopwords]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text =" ".join(text)
    return text
data["text"] = data["text"].apply(clean)

import  matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = " ".join(i for i in data.text)
dtopwords = set(STOPWORDS)
worldcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(15, 10))
plt.imshow(worldcloud, interpolation= 'bilinear')
plt.axis("off")
plt.show()


data["label"] = data["label"].map({0: "no Stress", 1: "Stress"})
data = data[["text", "label"]]
print(data.head())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import  train_test_split

x = np.array(data["text"])
y = np.array(data["label"])

cv = CountVectorizer()
X = cv.fit_transform(x)
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.33, random_state=42)


from sklearn.naive_bayes import BernoulliNB
model = BernoulliNB()
model.fit(xtrain, ytrain)

user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)


