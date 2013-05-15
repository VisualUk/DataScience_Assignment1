import json
import sys



''' open output.txt and create list '''
tweet_file = open(sys.argv[1])

alltweets = []
for line in tweet_file:
    alltweets.append(json.loads(line)) 
    
hash_list = []

for i in range(len(alltweets)):
    tweet = alltweets[i]
    if len(tweet) > 1:
        tweet = alltweets[i]['entities']  
        hashtag = tweet['hashtags']	
            
        if len(hashtag) > 0:	
            for i in range(0,len(hashtag)):	
                tag = hashtag[i]['text'].encode('utf-8')
                hash_list.append(tag)
     
#hashtags dict and  frequencies
hash_dict = {}	

for i in hash_list:
    if i in hash_dict.keys():	
        hash_dict[i] = hash_dict[i]+1
    else :
        hash_dict[i] = 1
   
#Sort hashtags by frequency and print top ten 
sorted_hash_list = []
    
for w in sorted(hash_dict, key=hash_dict.get,reverse=True)[0:10]:	 
    print str(w), float(hash_dict[w]) 






