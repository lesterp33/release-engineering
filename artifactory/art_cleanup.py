#!python3

# Clean up files in a given repo that match an AQL query

import json, requests, os, re

user = 
apikey = 
repo =
url = 'https://artifactory/api/search/aql'
rurl = 'https://artifactory/' + repo + '/'
payload = 'items.find( { "repo":{"$eq":"'+ repo + '"}, "created":{"$before":"180d"} } ).include("path")'
#files = {'file': open(aql, 'rb')}
headers = {'content-type':'text/plain'}
pattern = re.compile(r'Main')

r = requests.post(url, auth=(user, apikey), data=payload, headers=headers)
data = r.json()
#testitem = data['results'][0]['path']
#print(testitem)
results = data['results']
i = 0

for result in results:
    rpath = results[i]['path']
    basedir, subdir = result['path'].rsplit('/', 1)
    # if pattern.match(rpath):
    if basedir in ['dir1', 'dir2']:
      print(rpath)
    ## uncomment to delete
      durl = rurl + rpath
      print(durl)
      d = requests.delete(durl, auth=(user, apikey))
      print(d)
    i += 1