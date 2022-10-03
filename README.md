[![pipeline status](https://gitlab.com/gabriel_oana/worldoftanks/badges/master/pipeline.svg)](https://gitlab.com/gabriel_oana/worldoftanks)
[![pipeline status](https://gitlab.com/gabriel_oana/worldoftanks/badges/master/coverage.svg)](https://gitlab.com/gabriel_oana/worldoftanks)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/wotapi)](https://gitlab.com/gabriel_oana/worldoftanks)



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

```
from worldoftanks import WotAPI

wot = WotAPI(application_id='############',
             account_id='##########',
             token='#########',
             realm='eu')
```

```
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

##### Unittesting
For development purposes, the unittests can be executed via: 

```
python3 -m unittest discover -v worldoftanks/tests
```

##### Coverage Tests

```
coverage run --source=worldoftanks -m unittest discover -s worldoftanks/tests
coverage report -m
```
