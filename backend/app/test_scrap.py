import requests
import pandas as pd
import json

# uri = 'https://api.football-data.org/v4/matches'
# uri = 'https://api.football-data.org/v4/competitions/WC/standings'
uri = 'https://api.football-data.org/v4/competitions/WC/matches?status=FINISHED'
# uri = 'https://api.football-data.org/v4/competitions/WC/matches'
headers = {'X-Auth-Token': '2c3979682d2644eca41f45ac67475191'}

response = requests.get(uri, headers=headers)

data = response.json()
match_data = []
for match in data['matches']:
    home = match['homeTeam']['name']
    away = match['awayTeam']['name']
    winner_code = match['score']['winner']  # 'HOME_TEAM', 'AWAY_TEAM', 'DRAW', ou None

    if winner_code == 'HOME_TEAM':
        winner = home
    elif winner_code == 'AWAY_TEAM':
        winner = away
    elif winner_code == 'DRAW':
        winner = 'Match nul'
    else:
        winner = 'Inconnu'

    match_data.append([
        match['utcDate'],
        home,
        away,
        match['score']['fullTime']['home'],
        match['score']['fullTime']['away'],
        winner,
    ])

print(json.dumps(match_data, indent=4, ensure_ascii=False))
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