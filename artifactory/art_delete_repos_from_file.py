#!python3

# deletes list of repos from file

import json, requests, os, getpass
from pprint import pprint

user = 
apikey = 
#mypass = getpass.getpass()


with open ('repos.txt') as f:
    repos = f.read().splitlines()
print(repos)

for r in repos:
    print(r)
    durl = 'https://artifactory/api/repositories/' + r
    d = requests.delete(durl, auth=(user, apikeyx60))
    print(d)