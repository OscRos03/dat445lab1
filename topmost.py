import sys
import wordfreq
import urllib.request

stopwords = open(sys.argv[1])

n = int(sys.argv[3])

try:
    text = open(sys.argv[2])
except :
    response = urllib.request.urlopen(sys.argv[2])
    text = response.read().decode("utf8").splitlines()
else:
    text = open(sys.argv[2])



def main(stopwords, text,n ):
    words=wordfreq.tokenize(text)
    stopWords=wordfreq.tokenize(stopwords)
    frequencies=wordfreq.countWords(words, stopWords)
    
    wordfreq.printTopMost(frequencies, n)
    

main(stopwords, text,n)
