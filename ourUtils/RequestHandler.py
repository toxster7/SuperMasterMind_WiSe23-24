import requests
import json
from jsonschema import Draft7Validator
import sys
sys.path.append('../wise23-24_superhirn_25/')





class RequestHandler:
    """

    """

    def __init__(self, gamerid,code_len, n_colors,URL, Port):
        """

        """

        self.gameid = 0
        self.gamerid = gamerid
        self.positions = code_len
        self.colors = n_colors
        self.value = ""


        self.json_schema = ""
        self.postURL = URL
        self.postPort = Port

    def generate_json_template(self):
        self.readFile()
        template = {}
        for key, value in self.json_schema.items():
            if key == 'required':
                continue
            if isinstance(value, dict):
                if 'type' in value:
                    if value['type'] == 'string':
                        template[key] = ''
                    elif value['type'] == 'integer':
                        template[key] = 0
                    # Weitere Datentypen können hinzugefügt werden
                else:
                    template[key] = self.generate_json_template(value)
        return template

    def prepareJson(self, game_id,value):
        template = self.generate_json_template()
        template["gameid"] = game_id
        template["gamerid"] = self.gamerid
        template["positions"] = self.positions
        template["colors"] = self.colors
        template["value"] = value
        
        return template


    def eingabePOSTZiel(self, ziel, zielPort):
        """

        :param ziel:
        :return:
        """
        self.postURL = ziel
        self.postPort = zielPort

    def readFile(self):
        """

        :return:
        """
        with open("ourUtils/schema.json", "r", encoding="UTF8") as json_data:
            self.json_schema = json.load(json_data)
        json_data.close()
        #print(self.json_schema)

    #try with https://postman-echo.com/post
    def sendRequest(self, game_id,value):
        """

        :param gameid:
        :param gamerid:
        :param positions:
        :param colors:
        :param value:
        :return:
        """
        
        request = self.prepareJson(game_id,value)

        print(request)
        try:
            response = requests.post(self.postURL, json=request,
                                 headers={'Content-type': 'application/json; charset=utf-8'})
            print(response.json())
        except requests.RequestException as e:
            print(f"Error: {e}")

        '''
        try:
            response = requests.head(url, timeout=10)
            if response.status_code == 200:
                print(f"URL {url} is reachable.")
            else:
                print(f"URL {url} is not reachable. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")
    
        '''
        if response.status_code == 200:
            print("Zug erfolgreich abgeschickt")
            """
            print("___________")
            print(response.json)
            print("___________")
            print("___________")
            print(response.text)
            print("___________")
            """
        
        else:
            print(f"URL {url} is not reachable. Status code: {response.status_code}")
        
        return response.json()["json"]
        
    def getResponse(self, response):
        #responseJSON = json.load(response.json())
        responseJSON = self.json_schema
        self.gameid = responseJSON["gameid"]
        self.gamerid = responseJSON["gamerid"]
        self.positions = responseJSON["positions"]
        self.colors = responseJSON["colors"]
        self.value = responseJSON["value"]

        moveDict = {
            "gameid": self.gameid,
            "gamerid": self.gamerid,
            "positions": self.positions,
            "colors": self.colors,
            "value": self.value
        }
        #print(moveDict)
        return moveDict

'''
a = RequestHandler("flrnbr", 4, 4, 'https://postman-echo.com/post:8080', 4000)
a.readFile()
response = a.sendRequest(0,"Hallo")
print(response["gameid"])
print(response["gamerid"])
print(response["positions"])
print(response["colors"])
print(response["value"])
'''

