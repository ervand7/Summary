# import requests module
import requests

# Making a get request
response = requests.get('https://geeksforgeeks.org')

# print response
print(response)

# print history
print(response.history)