##Given a file of twitter stream (my sample is output.txt) and a dictionary of
##terms and their sentiments (AFINN-111.txt), this outputs the sentiment score for 
##all terms in the tweets, including new terms.

import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

##    load sentiment, use sent_file = "AFINN-111.txt"
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        if len(term.split()) > 1:
            del scores[term]

##    print scores

##    load twitter feed, use tweet_file = output.txt
    data = []
    output = open(sys.argv[2])
    for line in output:
        data.append(json.loads(line))

##    get tweets themselves tweets = [tweet, tweet, tweet]            
    tweets = []
    for i in range(len(data)):
        if "text" in data[i].keys():
            tweets.append(data[i]["text"].encode('utf-8'))

##    print tweets 

##    score the tweets, tweet_score = {tweet: score}
    tweet_score = {}
    word_tweet = {}
    for i in range(len(tweets)):
        tw = tweets[i].split() #re.findall(r"[\w']+", tweets[i]) #break tweets into words
        stw = []
        for w in range(len(tw)): #give each word a score, sum(stw)
            tw[w] = tw[w].lower() #lower case words
            if tw[w] in scores.keys():
                stw.append(scores[tw[w]])
            else:
                stw.append(0)
            #sum the word scores for each tweet
        tweet_score[tweets[i]] = sum(stw) #needs to be out of for-loop

##    for each word, list scores of tweets with word, word_tweet = {word:
##    [tweet score, tweet score, tweet score]}
        for w in range(len(tw)): #score 
            if tw[w] in word_tweet.keys():
                word_tweet[tw[w]].append(tweet_score[tweets[i]])
            else:    
                word_tweet[tw[w]] = [tweet_score[tweets[i]]]

##    print tweet_score

##    print word_tweet
    
##    append scores to include new words with their appropriate sentiment
##    score
    for i in range(len(word_tweet.keys())):
        if word_tweet.keys()[i] not in scores.keys():
            scores[word_tweet.keys()[i]] = float(sum(word_tweet[word_tweet.keys()[i]]))/float(len(word_tweet[word_tweet.keys()[i]]))            

##    print scores
    for i in range(len(scores.keys())):
        print scores.keys()[i], '%10f' % scores[scores.keys()[i]]

if __name__ == '__main__':
    main()
