import csv
from collections import defaultdict

#Distinct tracks played more than one
def distincTrackCounter(res):
    for element in res:
        res[element]=(len(set(res[element])))
    return res

#Calculate clients played same count of distict tracks
def countSamePlay(res):
    flipped = defaultdict(list)
    for key, value in res.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    for key, value in flipped.items():
        flipped[key]=(len(flipped[key]))
    return flipped

#Create csv file
def createCsv(resultDict):
    csv_file = "DistincTrack.csv"
    csv_columns = ['DISTINCT_PLAY_COUNT','CLIENT_COUNT']
    try:
        with open(csv_file,'w',newline ='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for key in resultDict.items():
                writer.writerow(key)
    except IOError:
        print("I/O error")

file = 'exhibitA-input.csv'
with open(file) as fh:
    rd = csv.reader(fh, delimiter='\t')
    res = defaultdict(list)
    for sid, tid, cid, date in rd:
        if (date[:10]=="10/08/2016"):
            res[cid].append(tid)
    resultDict=countSamePlay(distincTrackCounter(res))
    createCsv(resultDict)





