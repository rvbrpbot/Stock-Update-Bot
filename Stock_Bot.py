# -*- coding: utf-8 -*-
"""
Created on Mon Mar  14

@author: DapperDodger
"""
import praw
import yahoo_finance as yf
import obot_stock as obot
import re
import time
stock_name = "2498.TW"
company_name = "HTC Corp"
subreddit = "DapperDodger"
currency = "TWD"
sidebar_regex = re.compile("\|.*\|", re.MULTILINE)
r = obot.login()
stock = yf.Share(stock_name)

def get_up_or_down():
    open_price = stock.get_open()

    up_or_down = ''

    if open_price > stock.get_price():
        up_or_down = 'down'
    
    elif open_price < stock.get_price():
        up_or_down = 'up'
    
    else:
        up_or_down = 'even'
    
    return up_or_down
    
def build_response():
    up_down = get_up_or_down()
    stock_time = "Stock current as of: " + stock.get_trade_datetime()
    stock_time = stock_time[:-5]
    percent = stock.get_change() + "%"
    line = "\n\n---------------------------------------------\n\n"
    
    response = "|" + company_name + "\n\n" + stock_name + "\n\n" + up_down + " " + stock.get_price() + " " + currency + " "+ percent + line + stock_time + "|"
        
    return response
    
if __name__=="__main__":
    while(True):
        try:
            stock.refresh()
            sidebar_contents = r.get_wiki_page(subreddit, 'config/sidebar')
            new_contents = build_response()
            text = sidebar_contents.content_md
            text = sidebar_regex.sub(new_contents, text)  
            print text
            sidebar_contents.edit(text)
            time.sleep(30)
        except praw.errors.HTTPException:
            print "Http error, retrying..."