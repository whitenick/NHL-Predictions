import pandas as pd
import requests
import json

def prettify(jsonString):
    return json.loads(jsonString)

nhl_games = "https://statsapi.web.nhl.com/api/v1/teams"
response = requests.request("GET", nhl_games)

jsonResp = prettify(response.text)

teams = jsonResp["teams"]
teamFrame = pd.read_json(json.dumps(teams))

print(teamFrame)


