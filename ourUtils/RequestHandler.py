import requests
import json
import random
from jsonschema import Draft7Validator
from urllib.parse import urlparse, urlunparse
import sys
sys.path.append('../wise23-24_superhirn_25/')
from ourUtils.Pseudoserver import Pseudoserver

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
        self.postURL = self.generateURLwitPort(URL,Port)
        self.postPort = Port

        self.ps = Pseudoserver()
        

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

        #print(request)
        try:
            response = requests.post(self.postURL, json=request, timeout=5,
                                 headers={'Content-type': 'application/json; charset=utf-8'})
            print(response.json())

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
                with open('response.txt', 'a') as file:
                    file.write(response.text)
                    file.write('\n')
                    print("Response erfolgreich in response.txt geschrieben.")
                
                return response.json()
            
            else:
                print(f"URL {self.postURL} is not reachable. Status code: {response.status_code}")

        except requests.Timeout:
            print(f"URL {self.postURL} is not reachable. Timeout")
            print(f"Connecting to Pseudoserver...")
            
            return self.ps.respond(request)


        

        
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


    def generateURLwitPort(self,url_or_ip, port):
        parsed_url = urlparse(url_or_ip)

        # Überprüfen, ob der gegebene String eine IP-Adresse oder eine URL ist
        if parsed_url.netloc:
            # Der gegebene String ist eine URL
            new_netloc = f"{parsed_url.hostname}:{port}" if parsed_url.port is None else f"{parsed_url.hostname}:{port}"
            new_url = urlunparse((parsed_url.scheme, new_netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))

        else:
            # Der gegebene String ist eine IP-Adresse
            new_netloc = f"{url_or_ip}:{port}"
            return "".join(['http://',new_netloc])
            #new_url = urlunparse((parsed_url.scheme, new_netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))

        return new_url

'''
a = RequestHandler("flrnbr", 4, 4, '141.45.38.219', 5001)
a.readFile()
print(a.postURL)
#print(a.generateURLwitPort('127.0.0.1', 443))
#print(a.generateURLwitPort('https://www.postman-echo.com/post', 443))

response = a.sendRequest(0,"")
for i in range(10):
    code = [str(random.randint(1, 4)) for _ in range(4)]
    codestr = "".join(code)
    response = a.sendRequest(response["gameid"], codestr)
    print(response["gameid"])
    print(response["gamerid"])
    print(response["positions"])
    print(response["colors"])
    print(response["value"])
'''