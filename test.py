import base64
import json

import jwt


print("Testing JWT token verification...")

jwt_token = ''

def decode_jwt(token):
    token_payload = token.split('.')[1]
    # Add padding if necessary
    rem = len(token_payload) % 4
    if rem > 0:
        token_payload += '=' * (4 - rem)
    decoded_token = json.loads(base64.urlsafe_b64decode(token_payload).decode('utf-8'))
    return decoded_token

def decode_jwt_with_key(token, key):
    decoded_token = jwt.decode(jwt_token, key, algorithms=['HS256'])
    return decoded_token

def get_auth_provider(decoded_token):
    if 'authProvider' in decoded_token:
        return decoded_token['authProvider']
    
    if 'iss' in decoded_token and decoded_token['iss'].startswith('https://accounts.google.com'):
        return 'google'

    return 'custom'

decoded_token = decode_jwt(jwt_token)
auth_provider = get_auth_provider(decoded_token)

# if the auth_provider is 'google', do a google auth check

print(auth_provider)
print(decoded_token)
