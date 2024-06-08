from requests_oauthlib import OAuth2Session
# Replace these values with your OAuth provider's details
client_id = 'your_client_id'
client_secret = 'your_client_secret'
authorization_base_url = 'https://provider.com/oauth/authorize'
token_url = 'https://provider.com/oauth/token'

# Creating an OAuth session
oauth = OAuth2Session(client_id, redirect_uri='http://your-redirect-uri.com')

# Fetch the authorization URL
authorization_url, state = oauth.authorization_url(authorization_base_url)

# Have the user authorize your app and fetch the access token
print('Please go to %s and authorize access.' % authorization_url)
authorization_response = input('Enter the full callback URL: ')
token = oauth.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# Now you can use the token to make authorized requests
response = oauth.get('https://provider.com/api/resource')
print(response.json())

