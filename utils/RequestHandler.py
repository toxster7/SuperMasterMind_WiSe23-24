import requests
import json


class RequestHandler:
    """

    """

    def __init__(self):
        """

        """

        self.gameid = ""
        self.gamerid = ""
        self.positions = ""
        self.colors = ""
        self.value = ""


        self.json_schema = ""
        self.postURL = "http://localhost:8080"

    def eingabePOSTZiel(self, ziel):
        """

        :param ziel:
        :return:
        """
        self.postURL = ziel

    def readFile(self):
        """

        :return:
        """
        with open("schema.json", "r", encoding="UTF8") as json_data:
            self.json_schema = json.load(json_data)
        json_data.close()
        # print(self.json_schema)

    def sendRequest(self, gameid, gamerid, positions, colors, value):
        """

        :param gameid:
        :param gamerid:
        :param positions:
        :param colors:
        :param value:
        :return:
        """
        #
        self.json_schema["gameid"]["type"] = gameid
        self.json_schema["gamerid"]["type"] = gamerid
        self.json_schema["positions"]["type"] = positions
        self.json_schema["colors"]["type"] = colors
        self.json_schema["value"]["type"] = value

        response = requests.post(self.postURL, json=self.json_schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})

        if response.status_code == 200:
            print("Zug erfolgreich abgeschickt")
            #print("___________")
            #print(response.json)
            #print("___________")
            self.getResponse(response)


        else:
            print("Zug nicht erfolgreich abgeschickt. Status: " + str(response.status_code))

    def getResponse(self, response):
        responseJSON = json.load(response.json())
        #responseJSON = self.json_schema
        self.gameid = responseJSON["gameid"]["type"]
        self.gamerid = responseJSON["gamerid"]["type"]
        self.positions = responseJSON["positions"]["type"]
        self.colors = responseJSON["colors"]["type"]
        self.value = responseJSON["value"]["type"]

        moveDict = {
            "gameid": self.gameid,
            "gamerid": self.gamerid,
            "positions": self.positions,
            "colors": self.colors,
            "value": self.value
        }
        print(moveDict)
        return moveDict


a = RequestHandler()
a.readFile()
a.sendRequest(55, "Ilai", 4, 4, "Valie")
