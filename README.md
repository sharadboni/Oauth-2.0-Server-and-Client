# Oauth-2.0-Server-and-Client

Full Oauth 2.0 ecosystem

# Development

1. make develop
2. . ./venv/bin/activate
3. pre-commit install

# Overview of Oauth 2.0 protocol

1. User(Resource Owner) tells the Client that Client can act on behalf of the User.
2. Client asks User(Resource Owner) to authorize it on the Authorization Server.
3. User(Resource Owner) authorizes Client to take actions on its behalf.
4. Authorization Server supplies a token to Client because the User granted the authorization.
5. Client presents this Token to Protected Resource every time it wants to take actions on behalf of the user.

# Authorization Grant
