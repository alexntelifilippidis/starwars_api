import requests
import datetime
import json
import os

def print_data(world_flag, response):
    if world_flag == False:

        if response['result']:
                    print('Name:'+response['result'][0]['properties']['name'])
                    print('Height:'+response['result'][0]['properties']['height'])
                    print('Mass:'+response['result'][0]['properties']['mass'])
                    print('Birth Year:'+response['result'][0]['properties']['birth_year'])

        else:
                    print('The force is not strong within you')
    else:
        if response['result']:
                    print('Name:' + response['result'][0]['properties']['name'])
                    print('Height:' + response['result'][0]['properties']['height'])
                    print('Mass:' + response['result'][0]['properties']['mass'])
                    print('Birth Year:' + response['result'][0]['properties']['birth_year'])
                    print('Homeworld')
                    print('----------------')
                    print('Name:' + response['home'])
                    print('Population:' + response['population'])
                    print('')
                    city = response['home']
                    years = str(round(int(response['years'])/365, 2))
                    days = str(round(int(response['days'])/24, 2))
                    print(f'On {city}, 1 year on earth is {years} years and 1 day {days} days')
                    try:
                        cached = response['timestamp']
                        print(f'cached:{cached}')
                    except:
                        pass
        else:
                    print('The force is not strong within you')

def search(name, world_flag=False):
    response = []
    cache = open("data.json", "r")
    for i in cache:
        try:
            y = json.loads(i)
            if name.lower() in y['result'][0]['properties']['name'].lower():
                if response:
                    pass
                else:
                    response = y
        except:
            pass
    if response:
        print_data(world_flag, response)
    else:
        response = requests.get(f'https://www.swapi.tech/api/people/?name={name}')
        response2 = requests.get(response.json()['result'][0]['properties']['homeworld'])
        response = response.json()
        response2 = response2.json()
        response['home'] = response2['result']['properties']['name']
        response['population'] = response2['result']['properties']['population']
        response['years'] = response2['result']['properties']['orbital_period']
        response['days'] = response2['result']['properties']['rotation_period']
        response['timestamp'] = str(datetime.datetime.now())

        with open("data.json", "a") as myfile:
                cache = json.dumps(response)
                myfile.write(cache)
                myfile.write("\n")
        print_data(world_flag, response)

def cache(name, clean_flag=False):
    try:
        os.remove("data.json")
    except OSError:
        pass
    with open("data.json", 'a') as results_file:
        results_file.write(' \n')

def view(name):
    response = []
    count = 0
    cache = open("data.json", "r")

    for i in cache:
        if i.strip():
            y = json.loads(i)
            if name.lower() in y['result'][0]['properties']['name'].lower():
                count = count + 1
                if response:
                    pass
                else:
                    response = y

            print(f'The searches made:{count}')
            print('----------------')
            print_data(False, response)
            print('----------------')
            print(f'Time of the search:{str(datetime.datetime.now())}')
        else:
            pass
