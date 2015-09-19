import re
import csv
import json
import os
reader = open('/Users/eihli/Projects/private_sample_data/hr32.csv')

# Set up our result json object
result = {
  "technical_refusals": {},
  "interpersonal_refusals": {},
  "affinities": {}
}

responseMap = {
  "A": result["affinities"],
  "I": result["interpersonal_refusals"],
  "T": result["technical_refusals"]
}
# Get the names of each person from the header.
reader.next()
header = reader.next().strip().split(',')[1:]
# print "header lenght" + str(len(header))
for survey in result:
  for name in header:
    result[survey][name] = []
# print result

for row in reader:
  row = row.strip().split(',')
  name = row[0]
  print row
  row = row[1:]
  print row
  for i in range(len(row)):
    cell = str(row[i]).strip()
    for char in cell:
      if char in responseMap:
        if not responseMap[char][name]:
          responseMap[char][name] = []
        responseMap[char][name].append(header[i])
# print result
# print json.dumps(result, indent=2, separators=(',', ': '))
f = open('/Users/eihli/Projects/private_sample_data/class.json', 'w')
f.write(json.dumps(result, indent=2, separators=(',', ': ')))

  # print row


# for row in reader:
  # print row.split(',')
