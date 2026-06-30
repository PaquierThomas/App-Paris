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
            "équipe domicile": match["homeTeam"]["shortName"],
            "équipe extérieure": match["awayTeam"]["shortName"],
            "équipe extérieure id": match["awayTeam"]["id"],
            "date": match["utcDate"],
            "compétition": match["competition"]["name"],
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


@dlt.source
def coupe_du_monde():
    return [
        prochains_matchs(),
        classement_coupe_du_monde(),
    ]
