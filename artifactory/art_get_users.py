#!python3

# Gets the list of users from a given Artifactory instance

import json, requests, os, getpass
from pprint import pprint

mypass = getpass.getpass()

r = requests.get('https://artifactory/api/security/users', auth=(user, mypass ))
data = r.json()
type(data)
pprint(data)
# for user in data:
#     realm = user["realm"]
#     if realm == 'ldap':
#         print(user["name"])

