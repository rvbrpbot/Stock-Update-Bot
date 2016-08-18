# -*- coding: utf-8 -*-
"""
Created on Thurs Aug 18

@author: DapperDodger
"""

app_id = 'OUTYzb31qtssQg'
app_secret = 'szYYwtjBhfcKrsiayt_jZ8fnKFE'
app_uri = 'https://127.0.0.1:65010/authorize_callback'
app_ua = 'This is a sidebar updater for use by /r/RvBRP'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = 'Ahs-WZPELfjxP-4FF--TwgpQQrg'
app_refresh = '61586607-b-Bco0J2CcLK2H00b9HfG7IB6Rg'

import praw
def login():
    r = praw.Reddit(app_ua)
    r.set_oauth_app_info(app_id, app_secret, app_uri)
    r.refresh_access_information(app_refresh)
    return r

