import requests
import pandas as pd
import json

uri = 'https://api.football-data.org/v4/matches'
# uri = 'https://api.football-data.org/v4/competitions/WC/matches'
headers = {'X-Auth-Token': '2c3979682d2644eca41f45ac67475191'}

response = requests.get(uri, headers=headers)

match_data = []

# prochains matchs
# for match in response.json()['matches']:
#     match_data.append([
#         match["competition"]["name"],
#         match["homeTeam"]["shortName"],
#         match["awayTeam"]["shortName"],
#         match["season"]["startDate"],
#         match["season"]["endDate"],
#     ])

for match in response.json()['matches']:
    match_data.append([
        match["homeTeam"]["shortName"],
        match["awayTeam"]["shortName"],
        match["utcDate"]        
    ])

print(json.dumps(match_data, indent=4))

# df = pd.DataFrame(match_data, columns=["compétition","équipe domicile", "équipe extérieure", "date début saison", "date fin saison"])
# print(df)