import re
import csv
import json
import os
reader = open(os.path.dirname(__file__) + '/sampleData1.csv')

# Set up our result json object
result = {
  "technical_refusals": {},
  "interpersonal_refusals": {},
  "affinities": {}
}

responseMap = {
  "I would especially enjoy working with this person.": result["affinities"],
  "I would refuse to work with this person due to OUR INTERPERSONAL ISSUES": result["interpersonal_refusals"],
  "I would refuse to work with this person due to THEIR TECHNICAL ABILITIES": result["technical_refusals"]
}
# Get the names of each person from the header.
header = reader.next().strip().split(',')[1:]
# print "header lenght" + str(len(header))
for survey in result:
  for name in header:
    result[survey][name] = []
# print result

for row in reader:
  row = row.strip().split(',')
  name = row[0]
  row = row[1:]
  for i in range(len(row)):
    print row[i]
    if row[i] in responseMap:
      if not responseMap[row[i]][name]:
        responseMap[row[i]][name] = []
      responseMap[row[i]][name].append(header[i])
# print result
print json.dumps(result, indent=2, separators=(',', ': '))
f = open('class.json', 'w')
f.write(json.dumps(result, indent=2, separators=(',', ': ')))

  # print row


# for row in reader:
  # print row.split(',')
