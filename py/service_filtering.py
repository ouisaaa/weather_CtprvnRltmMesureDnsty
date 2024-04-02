import json

class Filtering:
    def filter_response_nei(self, nei, in_json):
        data=in_json

        # print(data["response"]["body"]["items"][0])

        for data in data["response"]["body"]["items"]:
            if data["stationName"]==nei:
                return data