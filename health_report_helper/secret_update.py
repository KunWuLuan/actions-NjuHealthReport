# Copyright 2022 kunwuluan. All Rights Reserved.
# Author-Github: github.com/kunwuluan
# secret_update.py 2022/4/14 13:01

import requests
from base64 import b64encode
from nacl import encoding, public
import json

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

def update_secret(token: str, git_account: str, git_username: str, secret_name: str, value: str):
    session = requests.Session()
    session.auth = (git_account, token)
    resp = session.get('https://api.github.com/user')
    resp = session.get('https://api.github.com/repos/{}/actions-NjuHealthReport/actions/secrets/public-key'.format(git_username))

    info = json.loads(resp.content)
    data = '{"encrypted_value":"'+encrypt(public_key= info['key'], secret_value= value)+'","key_id":"'+info['key_id']+'"}'

    resp = session.put('https://api.github.com/repos/{}/actions-NjuHealthReport/actions/secrets/{}'.format(git_username, secret_name), data=data, headers={'accept':'application/vnd.github.v3+json'})
    