##Given a file of twitter stream (my sample is output.txt) and a dictionary of
##terms and their sentiments (AFINN-111.txt), this outputs the happiest USA
##state in the tweets.

import sys
import json
import re

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    
##    load sentiment, use sent_file = "AFINN-111.txt"
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

##    load twitter feed, use tweet_file = output.txt
    data = []
    output = open(sys.argv[2])
    for line in output:
        data.append(json.loads(line))

##    list of US states for reference
    states_US = {"Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"}


##    get tweets themselves, encode them

##    didn't pick up any tweets-- why?
    
    tweets = []
    
    state_tweet = {} #{state: [tweet, tweet, tweet]}
    for i in range(len(states_US.values())):
        state_tweet[states_US.values()[i]] = [] #make sure that all states are accounted for

##    print state_tweet

    for i in range(len(data)):
        if "text" in data[i].keys():
            if "place" in data[i].keys():
                if data[i]["place"] != None:
                    if "country_code" in data[i]["place"].keys():
                        if data[i]["place"]["country_code"] == "US":
                            t = data[i]["text"].encode('utf-8')
                            tweets.append(t)
                            city_state = re.findall(r"[\w']+", data[i]["place"]["full_name"])
                            for j in range(len(city_state)):
                                if city_state[j] in state_tweet.keys():
                                    state_tweet[city_state[j]].append(t)
                                elif city_state[j] in states_US.keys():
                                    state_tweet[states_US[city_state[j]]].append(t)
                elif data[i]["place"] == None:
                    t = data[i]["text"].encode('utf-8')
                    tweets.append(t)
                    loc = re.findall(r"[\w']+", data[i]["user"]["location"])
                    if len(loc) > 0:
                        for j in range(len(loc)):
                            if loc[j] in state_tweet.keys():
                                state_tweet[loc[j]].append(t)
                            elif loc[j] in states_US.keys():
                                state_tweet[states_US[loc[j]]].append(t)
                                               
                                    
##    print len(tweets)
    
##    print state_tweet

##    sum of sentiment scores for all tweets from each state
    state_score = state_tweet.copy() #will be {state: [score, score, score]}
    for state in state_score:
        if len(state_score[state]) == 0:
            state_score[state] = 0
        else:
            for tweet in range(len(state_score[state])):
                tw = state_score[state][tweet].split() #re.findall(r"[\w']+", tweets[i]) #break tweets into words
                stw = []
                for w in range(len(tw)): #give each word a score, sum(stw)
                    tw[w] = tw[w].lower() #lower case words
                    if tw[w] in scores.keys():
                        stw.append(scores[tw[w]])
                    else:
                        stw.append(0)
            #sum the word scores for each tweet
                state_score[state][tweet] = sum(stw)
            state_score[state] = sum(state_score[state])
            

##    print state_score

##    need to get max score and print out corresponding state
    
    max_score = 0
    max_state = None
    for state in state_score:
        if state_score[state] > max_score:
            max_score = state_score[state]
            max_state = state

    print max_state
    

if __name__ == '__main__':
    main()
