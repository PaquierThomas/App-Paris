import requests
import pandas as pd
import json

uri = 'https://api.football-data.org/v4/matches'
headers = {'X-Auth-Token': '2c3979682d2644eca41f45ac67475191'}

response = requests.get(uri, headers=headers)

match_data = []
for match in response.json()['matches']:
    match_data.append([
        match["competition"]["name"],
        match["homeTeam"]["shortName"],
        match["awayTeam"]["shortName"],
        match["season"]["startDate"],
        match["season"]["endDate"],
    ])

df = pd.DataFrame(match_data, columns=["compétition","équipe domicile", "équipe extérieure", "date début saison", "date fin saison"])
print(df)