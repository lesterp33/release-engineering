#!python3

# Archives channels from given file

import json, requests, os
from pprint import pprint

access_token = 'xoxp-blah'
headers = {'Authorization': 'Bearer {}'.format(access_token)}
#channel_name = 'channelname'

with open ('channels.txt') as f:
    channels = f.read().splitlines()
# print(channels)

for c in range(len(channels)):
    r = requests.post('https://slack.com/api/admin.conversations.search?query=' + channels[c] + '&pretty=1&limit=1', headers=headers)
    data = r.json()
    channel_id = data['conversations'][0]['id']
    channel_name = data['conversations'][0]['name']
    print('Archiving ' + channel_name + ' ' + channel_id + ' : ')
    a = requests.post('https://slack.com/api/admin.conversations.archive?channel_id=' + channel_id + '&pretty=1', headers=headers)
    archive_response = a.status_code
    print(archive_response)