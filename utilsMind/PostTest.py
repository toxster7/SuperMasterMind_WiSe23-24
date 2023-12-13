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
        self.response = ""


        self.json_schema = ""
        self.postURL = "http://localhost"
        self.postPort = "8080"
        self.schema = ""

        print("Leer")
        self.sendEmptyPost()
        with open('regLog\LEER.txt', 'a') as f:
            f.write('::EMPTYJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestDiffSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\LEER.txt', 'a') as f:
            f.write('::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequest(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\LEER.txt', 'a') as f:
            f.write('::VORGABEJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestLowSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\LEER.txt', 'a') as f:
            f.write('::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')



        print("Korrekte Eingabe")
        self.gameid = 0
        self.gamerid = "Korrekte Eingabe"
        self.positions = 5
        self.colors = 4
        self.value = "12344,87877"

        with open('regLog\KORREKTEEINGABE.txt', 'a') as f:
            f.write('::EMPTYJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestDiffSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTE EINGABE.txt', 'a') as f:
            f.write('::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequest(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTE EINGABE.txt', 'a') as f:
            f.write('::VORGABEJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestLowSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTE EINGABE.txt', 'a') as f:
            f.write('::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')

        print("Korrekte Eingabe Strings")
        self.gameid = "1"
        self.gamerid = "Korrekte Eingabe Strings"
        self.positions = "3"
        self.colors = "3"
        self.value = "123,787"

        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write('::EMPTYJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestDiffSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write('::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequest(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write('::VORGABEJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestLowSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write('::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')

        print("Falsche Eingabe")
        self.gameid = "1"
        self.gamerid = "Korrekte Eingabe Strings"
        self.positions = "3"
        self.colors = "3"
        self.value = "123,787"

        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write(
                '::EMPTYJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestDiffSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write(
                '::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequest(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write(
                '::VORGABEJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')
        self.sendRequestLowSchema(self.gameid, self.gamerid, self.positions, self.colors, self.value)
        with open('regLog\KORREKTEEINGABESTRING.txt', 'a') as f:
            f.write(
                '::LOWSCHEMAJSON::\nPostJSON:\n' + self.schema + '\n---------\nResponse:\n' + self.response + '\n---------\n')

    def readfile(self):
        with open("schema.json", "r", encoding="UTF8") as json_data:
            self.json_schema = json.load(json_data)
        json_data.close()

    def getGoogle(self):
        response = requests.get("https://google.com")

    def sendEmptyPost(self):
        response = requests.post(self.postURL + ":" + self.postPort, json=self.json_schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})

    def sendRequest(self, gameid, gamerid, positions, colors, value):
        self.readfile()
        self.json_schema["gameid"]["type"] = gameid
        self.json_schema["gamerid"]["type"] = gamerid
        self.json_schema["positions"]["type"] = positions
        self.json_schema["colors"]["type"] = colors
        self.json_schema["value"]["type"] = value

        self.response = requests.post(self.postURL + ":" + self.postPort, json=self.json_schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})

    def sendRequestDiffSchema(self, gameid, gamerid, positions, colors, value):
        self.schema += "{" + "'gameid':" + "{'type':" + "{id}".format(id=gameid) + "},"
        self.schema += "" + "'gamerid':" + "{'type':'" + "{id}".format(id=gamerid) + "'},"
        self.schema += "" + "'positions':" + "{'type':" + "{id}".format(id=positions) + "},"
        self.schema += "" + "'colors':" + "{'type':" + "{id}".format(id=colors) + "},"
        self.schema += "" + "'value':" + "{'type':'" + "{id}".format(id=value) + "'}}"

        self.response = requests.post(self.postURL + ":" + self.postPort, json=self.schema,
                                 headers={'Content-type': 'application/json; charset=utf-8'})


    def sendRequestLowSchema(self, gameid, gamerid, positions, colors, value):
        self.schema += "{" + "'gameid':" + str(gameid) + ","
        self.schema += "" + "'gamerid':'" + gamerid + "',"
        self.schema += "" + "'positions':" + str(positions) + ","
        self.schema += "" + "'colors':" + str(colors) + ","
        self.schema += "" + "'value':'" + value + "'}"

        self.response = requests.post(self.postURL + ":" + self.postPort, json=self.schema,
                                         headers={'Content-type': 'application/json; charset=utf-8'})

