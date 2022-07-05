import requests


def nameAndStausDroplet(token, url):
    header = {'Authorization': f'Bearer {token}'}
    data = requests.get(url, headers=header).json()
    droplets = data['droplets']
    listOfDroplets = []
    for item in range(len(droplets)):
        status = droplets[item]['status']
        name = droplets[item]['name']
        listOfDroplets.append([name, status])
    return(listOfDroplets)
