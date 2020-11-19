import requests
from flask import Flask, redirect
from requests.models import PreparedRequest

TOKEN_ENDPOINT = 'localhost:8080/token'
REFRESH_ENDPOINT = 'localhost:8080/refresh'
AUTHORIZATION_ENDPOINT = 'localhost:8080/authorize'
CLIENT_ID = 'TEST_CLIENT_1'
# Never store secret in code. This is done just for illustration
CLIENT_SECRET = 'TEST_SECRET'
REDIRECT_URI = 'localhost:5000/callback'


# save this state on frontend, i.e htmlstorage and check it there
def _redirect(state):
    req = PreparedRequest()
    params = {'client_id': CLIENT_ID, 'response_type': 'code', 'redirect_uri': REDIRECT_URI, 'state': state}
    req.prepare_url(AUTHORIZATION_ENDPOINT, params)
    return redirect(req.url)


def _callback(code, grant_type='authorization_code'):
    response = requests.post(
        TOKEN_ENDPOINT,
        data={
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            grant_type: 'authorization_code',
            'code': code,
        },
    )
    resp_data = response.json()
    token = resp_data.get('access_token')
    refresh_token = resp_data.get('refresh_token')
    return token, refresh_token


def _refresh(refresh_token):
    refresh_token = ''
    _callback(code=refresh_token, grant_type='refresh_token')
