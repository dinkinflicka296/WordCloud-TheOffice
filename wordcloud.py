from wordcloud import WordCloud
import matplotlib.pyplot as plt


f = open('/kaggle/input/frequency-of-words-the-office/freq.txt', 'r')


word_frequency = {}
for line in f: 
    frequency = line.split(":")
    word_frequency[frequency[0]] = int(frequency[1])

removable_words = ['the', 'to', 'a', 'and', 'it', 'that', 'is', 'of', 'in', 'this', 'on', 'im', 'for', 'thats', 'itll', 'i',
                  'was', 'me', 'be', 'dont', 'we', 'he', 'get', 'you', 'no', 'what', 'not', 'my', 'have', 'do', 'just',
                  'so', 'are', 'its', 'your', 'but', 'at', 'with', 'youre']
for i in removable_words: 
    word_frequency.pop(i)
