##Given a file of twitter stream (my sample is output.txt) and a dictionary of
##terms and their sentiments (AFINN-111.txt), this outputs the sentiment score for 
##each of the tweets.

import sys
import json


def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    
    #load sentiment, use sent_file = "AFINN-111.txt"
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #load twitter feed, use tweet_file = output.txt
    data = []
    output = open(sys.argv[2])
    for line in output:
        data.append(json.loads(line))

    #get tweets themselves            
    tweets = []
    for i in range(len(data)):
        if "text" in data[i].keys():
            tweets.append(data[i]["text"]).encode('utf-8')
    
    #print tweets    
    
    tweet_score = []
    for i in range(len(tweets)):
        #break tweets into words
        tw = tweets[i].split(" ")
        stw = []
        #give each word a score
        for i in range(len(tw)):
            if tw[i].lower() in scores.keys():
                stw.append(scores[tw[i].lower()])
            else:
                stw.append(0)
        #sum the word scores for each tweet
        print '%10f' % sum(stw)
        #sys.stdout.write('%10f' % s)
        #tweet_score.append(sum(stw))
    

if __name__ == '__main__':
    main()
