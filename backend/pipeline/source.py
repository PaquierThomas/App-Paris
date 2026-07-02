import dlt
import requests

@dlt.resource(name="prochains_matchs", write_disposition="replace")
def prochains_matchs():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": "2c3979682d2644eca41f45ac67475191"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    for match in data["matches"]:
        yield {
            "id": match["id"],
            "equipe_domicile": match["homeTeam"]["shortName"],
            "equipe_exterieure": match["awayTeam"]["shortName"],
            "date": match["utcDate"],
            "stage": match["stage"],
        }


@dlt.resource(name="classement_coupe_du_monde", write_disposition="replace")
def classement_coupe_du_monde():
    url = "https://api.football-data.org/v4/competitions/WC/standings"
    headers = {"X-Auth-Token": "2c3979682d2644eca41f45ac67475191"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    for standing in data["standings"]:
        group = standing.get('group')
        for team_entry in standing['table']:
            yield {
                "compétition": data['competition']['name'],
                "groupe": group,
                "équipe": team_entry['team']['name'],
                "position": team_entry['position'],
                "points": team_entry['points'],
                "matchs_joués": team_entry['playedGames'],
                "victoires": team_entry['won'],
                "matchs_nuls": team_entry['draw'],
                "défaites": team_entry['lost'],
                "buts_marqués": team_entry['goalsFor'],
                "buts_encaissés": team_entry['goalsAgainst'],
            }

@dlt.resource(name="matchs_termines", write_disposition="replace")
def matchs_termines():
    url = "https://api.football-data.org/v4/competitions/WC/matches?status=FINISHED"
    headers = {'X-Auth-Token': '2c3979682d2644eca41f45ac67475191'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()



    for match in data["matches"]:
        home = match["homeTeam"]["name"]
        away = match["awayTeam"]["name"]
        winner_code = match["score"]["winner"]

        if winner_code == "HOME_TEAM":
            winner = home
        elif winner_code == "AWAY_TEAM":
            winner = away
        elif winner_code == "DRAW":
            winner = "Match nul"
        else:
            winner = "Inconnu"

        yield {
            "id": match["id"],
            "competition": data["competition"]["name"],
            "stade_competition": match["stage"],
            "groupe": match["group"],
            "date": match["utcDate"],
            "equipe_domicile": home,
            "equipe_exterieure": away,
            "buts_domicile": match["score"]["fullTime"]["home"],
            "buts_exterieur": match["score"]["fullTime"]["away"],
            "gagnant": winner,
            "statut": match["status"],
        }


@dlt.source
def coupe_du_monde():
    return [
        prochains_matchs(),
        classement_coupe_du_monde(),
        matchs_termines()
    ]
