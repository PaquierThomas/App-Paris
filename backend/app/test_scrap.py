import requests
import pandas as pd
import json

# uri = 'https://api.football-data.org/v4/matches'
uri = 'https://api.football-data.org/v4/competitions/WC/standings'
# uri = 'https://api.football-data.org/v4/competitions/WC/matches'
headers = {'X-Auth-Token': '2c3979682d2644eca41f45ac67475191'}

response = requests.get(uri, headers=headers)

data = response.json()
match_data = []

for standing in data['standings']:
    group = standing.get('group')
    for team_entry in standing['table']:
        match_data.append([
            data['competition']['name'],
            group,
            team_entry['team']['name'],
            team_entry['position'],
            team_entry['points'],
            team_entry['playedGames'],
            team_entry['won'],
            team_entry['draw'],
            team_entry['lost'],
            team_entry['goalsFor'],
            team_entry['goalsAgainst'],
        ])


print(json.dumps(match_data, indent=4))
# prochains matchs
# for match in response.json()['matches']:
#     match_data.append([
#         match["competition"]["name"],
#         match["homeTeam"]["shortName"],
#         match["awayTeam"]["shortName"],
#         match["season"]["startDate"],
#         match["season"]["endDate"],
#     ])


# df = pd.DataFrame(match_data, columns=["compétition","équipe domicile", "équipe extérieure", "date début saison", "date fin saison"])
# print(df)