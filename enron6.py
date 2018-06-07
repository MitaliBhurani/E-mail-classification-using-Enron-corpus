# Cleaning the data by converting it into lowercase, stemmed, lemmatized data and finding 100 most common words.

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
# import string

# For whole dataset's email body write this: with open("email_body.txt","r") as f
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
mscwords = frequency.most_common(1000)
nwords = len(mscwords)

# Dumping the most common 1000 words along with their frequency into pickle file
with open('ken.pickle', 'ab') as f1:
    a = [pickle.dump(mscw, f1) for mscw in mscwords]

with open('ken.pickle', 'rb') as f2:
    b = [pickle.load(f2) in range(nwords)]
    print(b)
