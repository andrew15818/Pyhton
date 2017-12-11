from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re

f = urllib.request.urlopen('https://docs.python.org/3/library/index.html')

word_freq = {}
word_freq_rank = []

for line in f:
    line = line.decode().strip()
    #print(line)
    if line.find('href=') != -1 and line.find('<li class') != -1:
        content = re.findall("</code> — ([^<]+)</a>", line)
        #print(content)
        if len(content) > 0:
            words = content[0].split()
            #print(words)
            for word in words:
                word_freq[word] = word_freq.get(word , 0)+1


for word, freq in word_freq.items():
    word_freq_rank.append((freq, word))
for freq, word in sorted(word_freq_rank, reverse=True)[:10]:
    print(word, freq)
