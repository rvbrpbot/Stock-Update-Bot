# -*- coding: utf-8 -*-
"""
Created on Thurs Aug 18

@author: DapperDodger
"""
import praw
import obot_RvB as obot
import re
import random
import time
subreddit = "dapperdodger"
weather_sidebar_regex = re.compile("\|(.|\s)*?\|", re.MULTILINE)
time_sidebar_regex = re.compile("(January|February|March|April|May|June|July|August|September|October|November|December)\s[0-9]{1,2}(st|nd|rd|th)\,\s[0-9]{4}\s[0-9]{1,2}\:[0-9]{2}(\s(PM|AM)){0,1}", re.MULTILINE)
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
    ("Clear", 500),
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
def get_time(time):
    minute = time[4]
    hour = time[3]
    minutestring = ""
    if(minute <10):
        minutestring = "0" + str(minute)
    else:
        minutestring = str(minute)
    if(hour <10):
        return " 0" + str(time[3]) +":" + minutestring
    else:
        return " " + str(time[3]) +":" + minutestring
    
        
def build_time():
    localtime = time.localtime(time.time())
    months = ["January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]
    suffix = ""
    day = localtime[2]
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    timestring = months[localtime[1]-1];
    timestring += " " + str(day) + suffix;
    timestring += ", " + str(int(localtime[0] + 550));
    timestring += get_time(localtime);
    return  timestring
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
    while True:
        try:
            sidebar_contents = r.get_wiki_page(subreddit, 'config/sidebar')
            
            new_time = build_time()
            text = sidebar_contents.content_md
            text = time_sidebar_regex.sub(new_time, text)
            print "The current time in Blood Gulch is: " + new_time
            if time.localtime(time.time())[3]==0 and time.localtime(time.time())[4] ==0:
                new_weather = build_response()
                text = weather_sidebar_regex.sub(new_weather, text) 
                print "The current weather in Blood Gulch is: " + new_weather
            
            sidebar_contents.edit(text)
        except praw.errors.HTTPException:
            print "Http error, retrying..."
        except Exception, e:
            print str(e)
        time.sleep(60);
        
        
    #testPercent()