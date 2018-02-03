#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import os
import twitter
import codecs

api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                  consumer_secret=os.environ.get('CONSUMER_SECRET'),
                  access_token_key=os.environ.get('ACCESS_TOKEN'),
                  access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
)
search = api.GetSearch(
    raw_query='l=en&q=%23superbowl%20since%3A2018-02-01%20until%3A2018-02-03&count=200'
)
print(len(search))


def write_data(file_name, cleaned_data):
    with codecs.open(file_name, 'wb', encoding='utf-8') as writen_file:
        writer = csv.writer(writen_file)
        for line in cleaned_data:
            writer.writerow([line])


d = os.path.dirname('/Users/mils/Projects/superbowl-hashtags/')
write_data(os.path.join(d, 'superbowl.txt'), search)
