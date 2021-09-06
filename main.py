import cbpro

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]
api_url = data[3]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase, api_url)

print(auth_client)

print(auth_client.get_accounts())
