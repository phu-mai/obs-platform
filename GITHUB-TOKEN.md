# How to generate SRE Github Token from Github App

SRE Github App credential is here <https://start.1password.com/open/i?a=AY7CIEE2INGCFPOFOE3OYQ2ITQ&v=27265wqp6mzm4rfqgk26dt5zmu&i=qk3pzildxkvlmfe7h6ktqxltpe&h=leapxpert.1password.com>

Install python library

```bash
pip install --no-cache-dir pyjwt requests cryptography
```

To generate Github Token from Github App, you can use below scripe

```python
#!/usr/bin/env python3

import sys
import jwt
import time
import os
import requests

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend

current_time = int(time.time())

app_id = "<input_github_app_id>"
organization = "<input_organization>" # e.g LeapXpert

payload = {
    # issued at time
    'iat': current_time,

    # JWT expiration time (10 minute maximum)
    'exp': current_time + (10 * 60),

    # GitHub App's identifier – you can get it from the github application dashboard
    'iss': app_id,
}

private_key_file_content = "<input_github_app_private_key>"

if private_key_file_content is not None:
    private_key_file_content=private_key_file_content.encode()

    cert_obj = load_pem_private_key(private_key_file_content, password=None, backend=default_backend())
    app_jwt = jwt.encode(payload, private_key_file_content, algorithm='RS256')

    headers_app_installations = {
        "Authorization": "Bearer " + app_jwt,
        "Accept": "application/vnd.github+json"
    }

    response_app_installations = requests.request("GET","https://api.github.com/app/installations", headers=headers_app_installations)

    for app_installation in response_app_installations.json():

        if(app_installation['account']['login'] == organization):
            app_installation_id = app_installation['id']

        headers_app_token = {
            "Authorization": "Bearer " + app_jwt,
            "Accept": "application/vnd.github+json"
        }

        resp_token = requests.request("POST","https://api.github.com/app/installations/" + str(app_installation_id) + "/access_tokens", headers=headers_app_token)
        encoded_app_token = resp_token.json()['token']
        print("Token: " + encoded_app_token)
```

Excecute the script to get Github token

```bash
python3 generate-jwt.py
```

Example to use generated Github Token in workflow as below with `SRE_GH_TOKEN` is defined in repository secret

```yaml
- name: Create Pull Request
  id: cpr
  uses: peter-evans/create-pull-request@v5
  with:
    token: ${{ secrets.SRE_GH_TOKEN }}
```
