import requests

response = requests.get('https://geeksforgeeks.org')

print(response)  # <Response [200]>
print(response.history)  # [<Response [301]>]
