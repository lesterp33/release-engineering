#!/bin/bash

# Get ssl cert from host
openssl s_client -showcerts -connect server.domain.com:636 </dev/null 2>/dev/null|openssl x509 -outform PEM >mycertfile.pem