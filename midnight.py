# Made by alporat.com
import json, io
from urllib.request import urlopen
from operator import itemgetter
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

scores = []

# Getting the data and putting it to a list with total score and the id
print("Starting Step 1...")
for i in range(10000):
    with urlopen('https://midnightsociety.com/founders_pass_json/' + str(i+1)) as f:
        data = json.load(f)    
    score = 0
    for att in data['attributes']:
        if att['trait_type'] != "Visor Cortex" and att['trait_type'] != "Rarity Class":
            score += float(att['score'])
    print("Currently at: " + str(i+1))
    scores.append([i+1, round(score, 2)])


# Sorting the list
print("Starting Step 2...")
sortedScores = sorted(scores, key=itemgetter(1), reverse=True)


# Adding the rank and naming to each element
print("Starting Step 3...")
finalScores = []
for i in range(len(sortedScores)):
    finalScores.append({"rank": i+1, "id": sortedScores[i][0], "total score": sortedScores[i][1]})


# Saving the final version as json
print("Starting Step 4...")
jsonScores = json.dumps(finalScores)
jsonFile = open("data.json", "w")
jsonFile.write(jsonScores)
jsonFile.close()

with io.open('dataWithSpacing.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(finalScores,
                      indent=4, sort_keys=False,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))