from pip._vendor import requests
API_KEY = "uNuYeA2IHXI3jBBE2tjiW3hOo8fkuxa2b3he7CclM2t1UJBZEuF8oRzLsRDdoGtiPCa0up7RBnRWrhNyFcmkkGnyt3F6QZbB4fZm7bH1qInply7j4NQ8fucf0O_hZXYx"
url = "https://api.yelp.com/v3/businesses/search"
file = open("rest.txt", mode="a", encoding="utf8")
headers = {'Authorization': f"Bearer {API_KEY}"}
params = {"term": "restaurants", 'location': "New York City", 'limit': 50}

response = requests.get(url, params=params, headers=headers)
print("This is response", response)
data = response.json()
print("This is json data:", data.keys())
print("This is json data:", type(data['businesses']))

for i in data['businesses']:
    try:
        name=i['name']
        address = i['location']['address1']
        print(name, address)
        try:
            cuisine = i['categories'][0]['alias']
            print(cuisine)
        except: 
            cuisine = 'no info'
    except: 
        print("didn't work for", i['name'])

    file.write(f"{name}, {address}, {cuisine} \n")
# try and except. Great way for error handling so that you can see what went wrong versus crashing entire program.
# try: 
#     number = 7 + '7'
# except:
#     number = 0
