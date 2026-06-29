import dlt
import requests

@dlt.resource(name="classement_cdm", write_disposition="replace")
def classement_coupe_du_monde():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": "2c3979682d2644eca41f45ac67475191"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    # À toi : inspecte data, trouve la bonne clé, et yield les éléments
    for match in data["matches"]:
        yield {
            "équipe domicile": match["homeTeam"]["shortName"],
            "équipe extérieure": match["awayTeam"]["shortName"],
            "équipe extérieure id": match["awayTeam"]["id"],
            "date": match["utcDate"],
            "compétition": match["competition"]["name"],
            "stage": match["stage"],
        }
