import requests
import json


class RequestHandler:
    """

    """

    def __init__(self):
        """

        """

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
        #print(self.json_schema)

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

        response = requests.post(self.postURL, json=self.json_schema,  headers={'Content-type': 'application/json; charset=utf-8'})

        if response.status_code == 200:
            print("Zug erfolgreich abgeschickt")
            print("___________")
            print(response.text)
            print("___________")

        else:
            print("Zug nicht erfolgreich abgeschickt. Status: " + str(response.status_code))

    def getRequest(self):
        """

        :return:
        """
        print("Hallo")


a = RequestHandler()
a.readFile()
a.sendRequest(55,"Ilai",4,4,"Valie")
