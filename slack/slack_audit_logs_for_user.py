#!python3

# Gets audit actions for a specific user id
import json, requests, os
from pprint import pprint

access_token = 'xoxp-blah'
headers = {'Accept': 'application/json','Authorization': 'Bearer {}'.format(access_token)}

r = requests.get('https://api.slack.com/audit/v1/logs?oldest=time&actor=userid&limit=20', headers=headers)
data = r.json()
pprint(data)