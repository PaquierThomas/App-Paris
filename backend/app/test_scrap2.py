import requests
import pandas as pd
import json

response = requests.get("https://www.thesportsdb.com/api/v1/json/123/lookuptable.php?l=4429&s=2026")
data = response.json()

print(response.status_code)

team_data = []
for team in data["table"]:
    team_data.append([
        team["strTeam"],
        team["intPlayed"],
        team["intWin"],
        team["intDraw"],
        team["intLoss"],
        team["intPoints"],
    ])


df = pd.DataFrame(team_data, columns=["équipe", "joues", "victoires", "nuls", "defaites", "points"])

print(df)