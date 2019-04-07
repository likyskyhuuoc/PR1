# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:37:23 2019

@author: Daura Hernández Díaz; Xiaowei Cai 
"""

import twitter
import json

#Please enter an absolute path where you would like to generate the results.
#For Windows users, the format of directory should be 'D:\\XXX\\XXX' or 'D:/XXX/XXX'. 
localdirection = "C:\\Users\\Xiaowei\\Desktop\\UOC学习\\Tipología y ciclo de vida de los datos\\Pr1\\"


q = input("Please enter the words you want to search in Twitter(A string):")

max_results = int(input("Please enter the maximum results you would like to have(An integer):"))

#Enter the credentials
CONSUMER_KEY =''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,
                     CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

#Check if the api is working properly.
print(twitter_api)

#Define a function to search tweets.
def twitter_search(twitter_api, q, max_results=200, **kw):
 
    search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    
    statuses = search_results['statuses']
    
    max_results = min(1000, max_results)
    
    for _ in range(10): 
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError as e: 
            break
            

        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        
        if len(statuses) > max_results: 
            break
            
    return statuses

#Create save function and load function    
def save_json(filename, data):
    #Specify the directory to save JSON file. 
    with open(localdirection+'{0}.json'.format(filename),
              'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def load_json(filename):
    #Specify the directory to load JSON file.
    with open(localdirection+'{0}.json'.format(filename), 
              'r', encoding='utf-8') as f:
        return json.load(f)


#Enter the contents for searching
results = twitter_search(twitter_api, q, max_results=5)


# Show one sample search result by slicing the list.
print(json.dumps(results[0], indent=1))

#Save the results into a local JASON file.
#save_json(q, results)

#Load the local JSON file
#results = load_json(q)

