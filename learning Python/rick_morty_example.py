from pip._vendor import requests
url = "https://rickandmortyapi.com/api/character/"    
file = open("r_m.txt", mode="a", encoding="utf8")

response = requests.get(url)
humans = []
aliens = []
data = response.json()

num_pages = data['info']['pages']
print(num_pages)

for i in data['results']:
    try:
        name = i['name']
        species = i['species']
        if species == "Human":
            humans.append(species)
        else:
            aliens.append(species)
        # print(f"{name} - {species}")
    except:
        print("oops")
        
    file.write(f"{name}, {species} Humans = {len(humans)} Aliens = {len(aliens)}\n")

print(len(humans))
print(len(aliens))

# There are 826 characters with 42 pages. get 2-3 more pages.