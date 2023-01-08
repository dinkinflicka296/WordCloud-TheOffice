from wordcloud import WordCloud
import matplotlib.pyplot as plt


f = open('freq.txt', 'r')


word_frequency = {}
for line in f: 
    frequency = line.split(":")
    word_frequency[frequency[0]] = int(frequency[1])

removable_words = ['the', 'to', 'a', 'and', 'it', 'that', 'is', 'of', 'in', 'this', 'on', 'im', 'for', 'thats', 'itll', 'i',
                  'was', 'me', 'be', 'dont', 'we', 'he', 'get', 'you', 'no', 'what', 'not', 'my', 'have', 'do', 'just',
                  'so', 'are', 'its', 'your', 'but', 'at', 'with', 'youre']
for i in removable_words: 
    word_frequency.pop(i)
    
wc = WordCloud(background_color="black",width=1000,height=1000,relative_scaling=0.2,normalize_plurals=False).generate_from_frequencies(word_frequency)
plt.imshow(wc)
