#!/usr/bin/env python

import twitter

CONSUMER_KEY = 'ujwr34Ctuz9QD1QWSrNIwncHp'
CONSUMER_SECRET = 'cENs3wRlTpNlHoCBCE7dns71q1dG2m3wWPricnBlyxyxd5AMm9'
OAUTH_TOKEN = '4268137473-KxAreuRmYiglsBylN6eUNsSApaZzDVTKoDNSYZ4'
OAUTH_TOKEN_SECRET = 'zhoGAbXvFHLfhTduIGnJ2PCrsVfg8X0VLSCK4H4u3LXKS'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)


'''
Unsure why I needed this now. Perhaps later to get WOE_IDs

Yahoo Client ID dj0yJmk9WU03Z0RCYTVtRjExJmQ9WVdrOVR6SllWRUpETjJVbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1kZA--
yahoo Client Secret 88f661cac7af208f45798c3a6846ef5fcd164580
'''

twitter_api = twitter.Twitter(auth=auth)
#print(twitter_api)
#print(world_trends)
#print()
#print(us_trends)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

"""
Display US trends
"""
print('US Trends')
for trend in us_trends[0]['trends']:
    print(trend['name'])

"""
Display World trends
"""
print('World Trends')
for trend in world_trends[0]['trends']:
    print(trend['name'])

"""
Set intersection. Trends common to both WORLD & US tweets
"""
world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)
print(common_trends)
