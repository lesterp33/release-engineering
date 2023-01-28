#!python3

# Example of getting folders that match a pattern and cleaning up

import json, re, requests, os

user =
apikey =
repo =
url = 'https://artifactory/api/storage/' + repo
rurl = 'https://artifactory/' + repo
turl = 'https://artifactory/api/trash/empty'
#payload = 'items.find( { "repo":{"$eq":"'+ repo + '"}, "created":{"$before":"90d"}, "stat.downloads":{"$lt":3} } ).include("path")'
#files = {'file': open(aql, 'rb')}
#headers = {'content-type':'text/plain'}

pattern = re.compile("^\/string-+")
# print(url)
r = requests.get(url)
data = r.json()
""" testitem = data['children'][0]['uri']
print(testitem) """
children = data['children']
i = 0

for child in children :
    rpath = children[i]['uri']
    # print(rpath)
    if pattern.match(rpath):
      print(rpath)
      durl = rurl + rpath
      print(durl)
      d = requests.delete(durl, auth=(user, apikey))
      print(d)
    i += 1

# Empty the trash
empty_trash = requests.post(turl, auth=(user, apikey))
print(empty_trash)