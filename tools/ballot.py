import glob
import json

csv_content = "state,timestamp,votes,eevp,trumpd,bidenj\r\n"

# read json files downloaded from https://static01.nyt.com/elections-assets/2020/data/api/2020-11-03/race-page/pennsylvania/president.json
# Note problem when total count is 2,984,468
for file in glob.glob("Input/*.json"):
    with open(file, encoding="utf8") as f:
        x = json.load(f)
    xts = x["data"]["races"][0]["timeseries"]
    for i in range(len(xts)):
        csv_content = csv_content + f'{file[:-5]},{xts[i]["timestamp"]},{xts[i]["votes"]},{xts[i]["eevp"]},{xts[i]["vote_shares"]["trumpd"]},{xts[i]["vote_shares"]["bidenj"]}\r\n'

# write csv table
with open('Output/result.csv', 'w', newline='') as f:
    f.write(csv_content)
