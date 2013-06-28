##Given a file of twitter stream (my sample is output.txt), this outputs the
##top ten hashtags.

import sys
import json
import re
import operator

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])

    data = []
    output = open(sys.argv[1])
    for line in output:
        data.append(json.loads(line))

    hashtags = {} #{tag: tally, tag: tally}

    #if there is a hashtag in a tweet, put the text of the hashtag into
    #hashtags with tally of 1 or tally the existing hashtag

    for i in range(len(data)):
        if "entities" in data[i].keys():
            if "hashtags" in data[i]["entities"]:
                if len(data[i]["entities"]["hashtags"]) > 0:
                    for j in range(len(data[i]["entities"]["hashtags"])):
                        tag = data[i]["entities"]["hashtags"][j]["text"]
                        if tag not in hashtags.keys():
                            hashtags[tag] = float(1)
                        else:
                            hashtags[tag] += float(1)


##    print hashtags

    sorted_hash = sorted(hashtags.iteritems(), key = operator.itemgetter(1), reverse = True)

    top_ten = sorted_hash[:10]

    for ht in top_ten:
    	print ht[0], ht[1]

if __name__ == '__main__':
    main()