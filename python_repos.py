import requests

# Make API Call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

response = requests.get(url, headers=headers)

print(f"Status Code:{response.status_code}")

# Store the value in variable as a dictionary object.
response_dict = response.json()
print(f"Total Repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories Returned: {len(repo_dicts)}")

# Examine the first repo
#repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}")

# for key in sorted(repo_dict.keys()):
#   print(key)
for repo_dict in repo_dicts:
    print(f"\n Selected Information About First Repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
