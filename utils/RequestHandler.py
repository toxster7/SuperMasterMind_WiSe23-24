import requests
import json

class RequestHandler:
    """

    """

    def __init__(self):
        """

        """

        self.json_schema = ""
        self.postURL = "https://localhost"


    def eingabePOSTZiel(self,ziel):
        """

        :param ziel:
        :return:
        """
        self.postURL = ziel

    def readFile(self):
        """

        :return:
        """
        with open("schema.json", "r") as json_data:
            self.json_schema = json.load(json_data)
        json_data.close()
        print(self.json_schema)

    def sendRequest(self, game_id, gamer_id, positions, colors, value):
        """

        :param game_id:
        :param gamer_id:
        :param positions:
        :param colors:
        :param value:
        :return:
        """
#
        self.json_schema["gameid"]["type"] = game_id
        self.json_schema["gamerid"]["type"] = gamer_id
        self.json_schema["positions"]["type"] = positions
        self.json_schema["colors"]["type"] = colors
        self.json_schema["value"]["type"] = value

        print(self.json_schema)

        #response = requests.post(self.postURL, self.json_schema)

        response = requests.get("https://google.com")
        print(response.text)

        if response.status_code == 200:
            print("Zug erfolgreich abgeschickt")
        else:
            print("Zug nicht erfolgreich abgeschickt. Status: " + response.status_code)

    def getRequest(self):
        """

        :return:
        """
        print("Hallo")

a=RequestHandler()
a.readFile()
a.sendRequest()
