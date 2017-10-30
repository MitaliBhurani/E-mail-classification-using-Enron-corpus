import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
# import string

with open("ken_lay_emails.txt", "r") as f:
    data = f.read()

words = word_tokenize(data)


ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

useful_words = [word for word in words if word not in stopwords.words('English')]

# useful_words1 = []
useful_words2 = []
'''for word in useful_words:
    useful_words1.append(ps.stem(word))'''

for word in useful_words:
    lower = word.lower()
    # no_punctuation = lower.translate(None,string.lower)
    if lower.isalnum():
        useful_words2.append(lemmatizer.lemmatize(lower))

frequency = nltk.FreqDist(useful_words2)

print(frequency.most_common(100))
