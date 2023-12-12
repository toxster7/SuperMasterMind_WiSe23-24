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
        self.postURL = "http://localhost"
        self.postPort = "8080"

    def eingabePOSTZiel(self, ziel, zielPort):
        """

        :param ziel:
        :return:
        """
        self.postURL = ziel
        self.postPort = zielPort

    def sendRequest(self, gameid, gamerid, positions, colors, value):
        """

        :param gameid:
        :param gamerid:
        :param positions:
        :param colors:
        :param value:
        :return:
        """
        self.schema += "{" + "'gameid':" + str(gameid) + ","
        self.schema += "" + "'gamerid':'" + gamerid + "',"
        self.schema += "" + "'positions':" + str(positions) + ","
        self.schema += "" + "'colors':" + str(colors) + ","
        self.schema += "" + "'value':'" + value + "'}"
        response = requests.post(self.postURL + ":" + self.postPort, json=self.schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})

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
            self.getResponse(response)
        else:
            print("Zug nicht erfolgreich abgeschickt. Status: " + str(response.status_code) +"\n"
                  + str(response) + "\n")

    def getResponse(self, response):
        self.gameid = response["gameid"]
        self.gamerid = response["gamerid"]
        self.positions = response["positions"]
        self.colors = response["colors"]
        self.value = response["value"]

        moveDict = {
            "gameid": self.gameid,
            "gamerid": self.gamerid,
            "positions": self.positions,
            "colors": self.colors,
            "value": self.value
        }

        return moveDict