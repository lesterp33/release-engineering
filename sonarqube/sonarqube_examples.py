#!python3
import json, requests, os, getpass
from pprint import pprint

headers = {'content-type':'application/json'}
# print(payload)
r = requests.get('https://sonarqube/api/projects/search?qualifiers=TRK', auth=('apikey', '' ), headers=headers)
data = r.json()
# pprint(data)
components=data['components']
# pprint(components)
# project_key=components[0]['key']
#print(project_key)
for c in components:
    project_key=c['key']
    # print(project_key)
    # get loc
    rloc = requests.get('https://sonarqube/api/measures/component?component=' + project_key + '&metricKeys=ncloc', auth=('apikey', '' ), headers=headers )
    locdata = rloc.json()
    try:
        ncloc=locdata['component']['measures'][0]['value']
    except IndexError:
        pass
    # for each in locdata['component']['key']['measures']:
    #     print (each['metric'])
    print('Project: ' + project_key + ' LOC: ' + ncloc)