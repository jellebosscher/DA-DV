# DA-DV
Data analytics and data visualization course for the Uva - Bachelor AI

Using data from https://github.com/jamesqo/gun-violence-data that in turn is
taken from http://www.gunviolencearchive.org/.
| field                   | type         | description
| required? |
|-----------------------------|------------------|-------------------------------------------------------------------------------|---------------|
| incident_id                 | int              |                 gunviolencearchive.org ID for incident| yes           |
| date                        | str|                           date of occurrence| yes           |
| state                       | str|                                                                               | yes
|
| city_or_county              | str|                                                                               | yes|
| address                     | str              | address where incident tookplace                                             | yes           |
| n_killed                    | int              | number of people killed| yes           |
| n_injured                   | int              | number of people injured| yes           |
| incident_url                | str              | link togunviolencearchive.org webpage containing details of incident         | yes|
| source_url                  | str              | link to online news story concerning incident                                 | no            |
| incident_url_fields_missing | bool             | ignore, always False | yes           |
| congressional_district      | int |                                                                               | no |
| gun_stolen                  | dict[int, str] | key: gun ID, value: 'Unknown' or 'Stolen'                                     | no            |
| gun_type                    | dict[int, str] | key: gun ID, value: description of gun type                                   | no            |
| incident_characteristics    | list[str]        | list of incident characteristics                                              | no            |
| latitude                    | float |                                                                               | no |
| location_description        | str              | description of location where incident took place                             | no            |
| longitude                   | float|                                                                               | no|
| n_guns_involved             | int              | number of guns involved | no            |
| notes                       | str              | additional notes about the incident                                           | no            |
| participant_age             | dict[int, int] | key: participant ID | no            |
| participant_age_group       | dict[int, str] | key: participant ID, value: description of age group, e.g. 'Adult 18+'        | no            |
| participant_gender          | dict[int, str] | key: participant ID, value: 'Male' or 'Female'                                | no            |
| participant_name            | dict[int, str] | key: participant ID | no            |
| participant_relationship    | dict[int, str] | key: participant ID, value: relationship of participant to other participants | no            |
| participant_status          | dict[int, str] | key: participant ID, value: 'Arrested', 'Killed', 'Injured', or 'Unharmed'    | no            |
| participant_type            | dict[int, str] | key: participant ID, value: 'Victim' or 'Subject-Suspect'                     | no            |
| sources                     | list[str]        | links to online news stories concerning incident                              | no            |
| state_house_district        | int |                                                                               | no |
| state_senate_district       | int |                                                                               | no |

