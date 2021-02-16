import config
import requests
from bs4 import BeautifulSoup
import csv
import re

# Filepath of mmsids
with open(r"test-10.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')

    for mmsid in reader:

        # mmsid = "9980376370502441"

        mmsid = re.sub(r"(\[')(\d+)('\])", r"\2", str(mmsid))

        queryURL = "https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/"

        apiKey = config.api_key

        response = requests.get(queryURL + mmsid + "?apikey=" + apiKey +  "&format=json")

        print(response.content)

        # soup = BeautifulSoup(response.content, 'html.parser')
        #
        # print(soup.record)
