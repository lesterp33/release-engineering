#!/bin/bash

curl -Lv https://jenkins/login 2>&1 | grep -i 'x-ssh-endpoint'
ssh -p 37717 jenkins help
ssh -p 37717 jenkins delete-builds "Folder/Job/branchjob" 230-280
