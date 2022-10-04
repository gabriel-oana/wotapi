<span><img src="https://img.shields.io/github/workflow/status/gabriel-oana/wotapi/Tests">
<img src="https://img.shields.io/github/languages/top/gabriel-oana/wotapi">
<img src="https://img.shields.io/pypi/pyversions/wotapi">
<img src="https://img.shields.io/pypi/v/wotapi">
<img src="https://img.shields.io/badge/linting-pylint-green">
[![Downloads](https://pepy.tech/badge/wotapi)](https://pepy.tech/project/wotapi)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<img src="https://img.shields.io/pypi/dm/wotapi?label=pypi%20downloads">
[![codecov](https://codecov.io/gh/gabriel-oana/wotapi/branch/test/badge/graph/badge.svg?token=5BW32QG1KJ)](https://codecov.io/gh/gabriel-oana/wotapi)
</span>

# World of Tanks - API (PC)

### 1. Description
This package will extract data from the Wargaming World of Tanks API.      
Currently, this works only for the PC version with the rest of the platforms to be implemented in future iterations.

The package will require the following from the official [World of Tanks Developer API](https://developers.wargaming.net/) page.
* application id
* account id
* access token

All data extracted will be written to a local sqlite database ready to be accessed. The database is automatically created
at the location where the script is executed.    
The name of the database is ```world_of_tanks.db``` of type sqlite.


### 2. Install

```
pip install WotAPI
```

### 3. Usage

```python
from wotapi import WotAPI, REALM

# Obtain the account id
# Since this is a constant it can be executed only once to get the account_id
wot = WotAPI(application_id='############', 
             realm=REALM.eu)
account_id = wot.get_account_id(nickname='username')


wot = WotAPI(application_id='############',
             account_id=account_id, 
             token='#########',
             realm='eu')

# Extract Account Data
wot.player_personal()
wot.player_vehicles()
wot.player_achievements()

# Extract Tankopedia Data
wot.tankopedia_vehicles(load_once=True)
wot.tankopedia_achievements(load_once=True)
wot.tankopedia_information(load_once=True)
wot.tankopedia_maps(load_once=True)
wot.tankopedia_badges(load_once=True)

# Extract Player Vehicles Data
wot.vehicle_achievements()
wot.vehicle_statistics()

# Renew access token
new_token_data = wot.renew_token()
print(new_token_data)
```


All data from the Tankopedia part of the API needs to be loaded only once in the database, otherwise this will be duplicated. 
For ease, the argument ```load_once``` is by default set to True. 

The data can be accessed from the ```wot``` objects for further development. The response is a list of dictionaries.
```
achievements = wot.player_achivements(load_once=True)
print(achievements)

[{
'name': 'medalBobAmway921', 
'outdated': True, 
'section': 'action', 
'section_order': 6, 
'image_big': 'http://api.worldoftanks.eu/static/2.66.0/wot/encyclopedia/achievement/big/medalBobAmway921.png', 
'hero_info': None, 
'name_i18n': None, 
'order': 1443, 
'type': 'single', 
'image': 'http://api.worldoftanks.eu/static/2.66.0/wot/encyclopedia/achievement/medalBobAmway921.png', 
'condition': 'None', 
'description': None
} ... 
]
```

To not load data in the database add the ```load_to_db=False``` argument to the WotAPI class parameters.
To give a specific location for the database to be created and populated set up the following arguments in the main class.

```
from worldoftanks import WotAPI

wot = WotAPI(application_id='####',
             account_id='##########',
             token='#########',
             realm='eu',
             load_to_db=True,
             db_path=<path_where_the_database_will_be_saved>,
             logging_enabled=True/False,
             log_level="WARNING"                     
    )
```



### 4. Left To Do

| API Part      | Name                      | Date Completed    | Version   |
| ---           | ---                       | ---               | ---       |
| Accounts      | Player Personal Data      | 2020-04-24        | 0.0.1     |
| Accounts      | Player Vehicles           | 2020-04-24        | 0.0.1     |
| Accounts      | Player Achievements       | 2020-04-24        | 0.0.1     |
| Tankopedia    | Vehicles                  | 2020-04-25        | 0.0.2     |
| Tankopedia    | Achievements              | 2020-04-25        | 0.0.2     |
| Tankopedia    | Tankopedia Information    | 2020-04-25        | 0.0.2     |
| Tankopedia    | Maps                      | 2020-04-25        | 0.0.2     |
| Tankopedia    | Badges                    | 2020-04-28        | 0.4.22    |
| Tankopedia    | Vehicle characteristics   |                   |           |
| Tankopedia    | Engines                   | Deprecated        |           |
| Tankopedia    | Turrets                   | Deprecated        |           |
| Tankopedia    | Radios                    | Deprecated        |           |
| Tankopedia    | Suspensions               | Deprecated        |           | 
| Tankopedia    | Guns                      | Deprecated        |           |
| Tankopedia    | Equipment and Consumables |                   |           |
| Tankopedia    | Personal Missions         |                   |           |
| Tankopedia    | Personal Reserves         |                   |           |
| Tankopedia    | Vehicle Configurations    |                   |           |
| Tankopedia    | Modules                   |                   |           |
| Tankopedia    | Crew Qualifications       |                   |           |
| Tankopedia    | Crew Skills               |                   |           |
| Vehicles      | Vehicle statistics        | 2020-04-27        | 0.3.2     |
| Vehicles      | Vehicle achievements      | 2020-04-27        | 0.3.2     |
| Clans         | Clans                     |                   |           |
| Clans         | Clan Details              |                   |           |
| Clans         | Clan Member Details       |                   |           |
| Clans         | Clan Glossary             |                   |           |
| Clans         | Message Board             |                   |           |
| Clans         | Player Clan History       |                   |           |
| Clan ratings  | Types of Ratings          |                   |           |
| Clan ratings  | Dates with available r.   |                   |           |
| Clan ratings  | Clan Ratings              |                   |           |
| Clan ratings  | Adj Positions In Clan R.  |                   |           |
| Clan ratings  | Top Clans                 |                   |           |
| Strongholds   |                           |                   |           |
| Global Map    |                           |                   |           |
    
 
### 5. Development
To further develop this package please follow the instructions below
```shell

# Install the virtual environments and packages
python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# Run test suite
# Tests contain unittests, coverage and linting
tox
```
