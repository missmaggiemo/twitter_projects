##Given a file of twitter stream (my sample is output.txt), this outputs the
##frequency of each term in the tweets.

import sys
import json

def main():
    
    tweet_file = open(sys.argv[1])
    word_freq = {}
    
##    load twitter feed, use tweet_file = output.txt
    data = []
    output = open(sys.argv[1])
    for line in output:
        data.append(json.loads(line))

##    get tweets themselves tweets = [tweet, tweet, tweet]            
    tweets = []
    for i in range(len(data)):
        if "text" in data[i].keys():
            tweets.append(data[i]["text"].encode('utf-8'))

##    split tweets into words, tally word count, word_tally = {word: int(freq)}
    word_tally = {}
    wcount = 0
    for i in range(len(tweets)):
        tw = tweets[i].split()
        wcount = wcount + len(tw)
        for w in range(len(tw)):
            tw[w] = tw[w].lower() #lower case words
            if tw[w] not in word_tally.keys(): #update word tally for each word
                word_tally[tw[w]] = 1
            else:
                word_tally[tw[w]] = word_tally[tw[w]] + 1
                
##    calculate word frequency, drop it into word_freq = {word: freq}, print
    for word in word_tally:        
        word_freq[word] = float(word_tally[word])/float(wcount) #calculate word frequency
        print word, '%10f' % word_freq[word] #print word, word frequency         
        

if __name__ == '__main__':
    main()

    
