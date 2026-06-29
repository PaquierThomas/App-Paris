import dlt
import requests

@dlt.resource(name="classement_cdm", write_disposition="replace")
def classement_coupe_du_monde():
    url = "https://www.thesportsdb.com/api/v1/json/123/lookuptable.php?l=4429&s=2026"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    # À toi : inspecte data, trouve la bonne clé, et yield les éléments
    for team in data["table"]:
        yield {
            "equipe": team["strTeam"],
            "joues": team["intPlayed"],
            "victoires": team["intWin"],
            "nuls": team["intDraw"],
            "defaites": team["intLoss"],
            "points": team["intPoints"],
        }

