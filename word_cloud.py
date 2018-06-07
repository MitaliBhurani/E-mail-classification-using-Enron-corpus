from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pickle
with open('total_words.pickle', 'rb') as f:
    list1 = [pickle.load(f) for i in range(1000)]
list_to_tuple = tuple(list1)
# print(list_to_tuple)
wordcloud = WordCloud(background_color='white', width=900, height=900).fit_words(dict(list1))
plt.figure(figsize=(20,20))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
