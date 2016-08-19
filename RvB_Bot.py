# -*- coding: utf-8 -*-
"""
Created on Thurs Aug 18

@author: DapperDodger
"""
import praw
import obot_RvB as obot
import re
import random
import sys
subreddit = "rvbrp"
sidebar_regex = re.compile("\|(.|\s)*?\|", re.MULTILINE)
r = obot.login()

"""50% chance of Clear Day, 
20% chance of Light Rain, 
10% chance of Thunderstorm/Heavy Rain, 
10% chance of Sandstorm, 
5% chance of Hail, 
and 5% chance of Tornado """
def weightedChoice(choices):
    """Like random.choice, but each element can have a different chance of
    being selected.

    choices can be any iterable containing iterables with two items each.
    Technically, they can have more than two items, the rest will just be
    ignored.  The first item is the thing being chosen, the second item is
    its weight.  The weights can be any numeric values, what matters is the
    relative differences between them.
    """
    space = {}
    current = 0
    for choice, weight in choices:
        if weight > 0:
            space[current] = choice
            current += weight
    rand = random.uniform(0, current)
    for key in sorted(space.keys() + [current]):
        if rand < key:
            return choice
        choice = space[key]
    return None
    
def getWeather(): 
    choices = [
    ("Sunny", 500),
    ("Light Rain", 200),
    ("Thunderstorm", 100),
    ("Sandstorm", 100) ,
    ("Hail", 50),
    ("Tornado", 50),
    ("Demonic Invasion", 5),
    ("Alien Invasion", 5)   
    
    ]
    return weightedChoice(choices)
    
def build_response():
    weather = getWeather();
    
    response = "| " + weather + " |"
        
    return response
def testPercent():
    weathers= {
         "Sunny": 0,
    "Light Rain": 0,
    "Thunderstorm": 0,
    "Sandstorm": 0,
    "Hail": 0,
    "Tornado": 0,
    "Demonic Invasion": 0,
    "Alien Invasion": 0     
    }
    for i in range (0, 365):
        weather = getWeather()
        weathers[weather] = weathers[weather]+1
    print weathers

   
if __name__=="__main__":
    
    try:
        sidebar_contents = r.get_wiki_page(subreddit, 'config/sidebar')
        new_contents = build_response()
        text = sidebar_contents.content_md
        text = sidebar_regex.sub(new_contents, text) 
        print "The current weather in Blood Gulch is: " + new_contents
        sidebar_contents.edit(text)
    except praw.errors.HTTPException:
        print "Http error, retrying..."
    except:
        e = sys.exc_info()[0]
        print  "Error: " + e;
        
    #testPercent()