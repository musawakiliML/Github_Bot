import requests

# Make API Call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

response = requests.get(url, headers=headers)

print(f"Status Code:{response.status_code}")

# Store the value in variable as a dictionary object.
response_dict = response.json()
print(response_dict.keys())
