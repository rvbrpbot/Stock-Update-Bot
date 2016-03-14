# -*- coding: utf-8 -*-
"""
Created on Mon Mar  14

@author: DapperDodger
"""

app_id = 'ik3AllijFPdIQw'
app_secret = 'atAB7zxgLYUTQ7Xf1K4zOqqlnCI'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'This is a sidebar updater for use by /r/htcinvestors'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'u_vMFjUfuIVrOpzsdZ49SY8136o'
app_refresh = '54399749-81mrTDWYlnFmz6PDVwGKv57ZE2o'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r

