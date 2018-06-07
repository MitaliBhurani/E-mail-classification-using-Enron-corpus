import pickle
from collections import Counter
import nltk
final_list = []


def merge(pickle_file):
    with open(pickle_file, 'rb') as f:
        for i in range(1000):
            final_list.append((pickle.load(f)))


merge('ken.pickle')
merge('chris.pickle')
merge('jeff.pickle')
merge('jeffrey.pickle')
merge('john.pickle')
merge('kay.pickle')
merge('richard.pickle')
merge('sara.pickle')
merge('steven.pickle')
merge('tana.pickle')
merge('vincent.pickle')

print(final_list)
print(len(final_list))
c = (Counter(dict(final_list))).most_common(1000)
with open('total_words.pickle', 'ab') as f1:
    a = [pickle.dump(mscw, f1) for mscw in c]
