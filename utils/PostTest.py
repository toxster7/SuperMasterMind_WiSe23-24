import requests
import json


class PostTest:

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
        self.schema = ""

    def readfile(self):
        with open("schema.json", "r", encoding="UTF8") as json_data:
            self.json_schema = json.load(json_data)
        json_data.close()
        # print(self.json_schema)

    def getGoogle(self):
        response = requests.get("https://google.com")
        with open('regLog\GETGOOGLE.txt', 'a') as f:
            f.write('::GOOGLEJSON::\n'
                    'Response:\n'
                    + str(response.text) +
                    '\n')

    def sendEmptyPost(self):
        response = requests.post(self.postURL + ":" + self.postPort, json=self.json_schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})
        with open('regLog\EMPTYJSON.txt', 'a') as f:
            f.write('::EMPTYJSON::\n'
                    'PostJSON:\n'
                    + self.json_schema +
                    '\n---------'
                    'Response:\n'
                    + response.text +
                    '\n')

    def sendRequest(self, gameid, gamerid, positions, colors, value):
        self.readfile()
        self.json_schema["gameid"]["type"] = gameid
        self.json_schema["gamerid"]["type"] = gamerid
        self.json_schema["positions"]["type"] = positions
        self.json_schema["colors"]["type"] = colors
        self.json_schema["value"]["type"] = value
        response = requests.post(self.postURL + ":" + self.postPort, json=self.json_schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})
        with open('regLog\SEINSCHEMAJSON.txt', 'a') as f:
            f.write('::SEINSCHEMAJSON::\n'
                    'PostJSON:\n'
                    + str(self.json_schema) +
                    '\n---------'
                    'Response:\n'
                    + response.text +
                    '\n')

    def sendRequestDiffSchema(self, gameid, gamerid, positions, colors, value):
        #self.readfile()
        self.schema += "{" + "'gameid':" + "{'type':" + "{id}".format(id=gameid) + "},"
        self.schema += "" + "'gamerid':" + "{'type':'" + "{id}".format(id=gamerid) + "'},"
        self.schema += "" + "'positions':" + "{'type':" + "{id}".format(id=positions) + "},"
        self.schema += "" + "'colors':" + "{'type':" + "{id}".format(id=colors) + "},"
        self.schema += "" + "'value':" + "{'type':'" + "{id}".format(id=value) + "'}}"

        response = requests.post(self.postURL + ":" + self.postPort, json=self.schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})
        with open('regLog\DIFFSCHEMAJSON.txt', 'a') as f:
            f.write('::DIFFSCHEMAJSON::\n'
                    'PostJSON:\n'
                    + str(self.schema) +
                    '\n---------'
                    'Response:\n'
                    + response.text +
                    '\n')


a = PostTest()
# a.getGoogle()
# a.sendEmptyPost()
#a.sendRequest(2, "Dart", 4, 5, "WERT")
#a.sendRequestDiffSchema(5, "Fluff", 5, 66, "BETRAG")
#a.sendRequest(5, "Fluff", 5, 66, "BETRAG")
a.sendRequestDiffSchema(2, "Dart", 4, 5, "WERT")
