import requests


def nameAndStausDroplet(token, url):
    # get info about all droplets
    droplets = requests.get(
        url, headers={'Authorization': f'Bearer {token}'}).json()['droplets']
    listOfDroplets = []
    # loop through all droplets
    for item in range(len(droplets)):
        # create list with name and status of each droplet
        listOfDroplets.append(
            [droplets[item]['name'], droplets[item]['status']])
    return(listOfDroplets)
