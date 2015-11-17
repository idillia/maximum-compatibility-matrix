import json
import copy
import time
from grouper.csv2json import csv2json
from grouper.arrangement import Arrangement
from grouper.group import Group
from grouper.participant import Participant
from grouper.strategy import Strategy
from grouper.arrangement2csv import arrangement2csv

# Constants
OUTPUT_FILENAME = "arrangement" # Right now, it will write to file the top 3 scoring arrangements
OUTPUT_FOLDER = '/Users/eihli/Projects/grouper/sample_data' # Rename this to your folder (or empty string '' to use current directory)
INPUT_CSV_FILENAME = "/Users/eihli/Projects/grouper/sample_data/class.csv" # Rename this to your CSV file. View readme for formatting rules.
TIMEOUT = 300 # in seconds
NUM_ITERATIONS = 10 # Higher number gives better groups but takes longer.
# NUM_PARTICIPANTS_PER_GROUP = 3 # This isn't working yet.

# TODO:
# Make work with groups of 4 with a few groups of 3.
# Make work with data directly as it comes from google survey.
# Write asana workflow for Shepherds
# Make work with weights for people who select too many friends.

# ------------- Genetic Algorithm. Random Swaps -------------#
def genetic(arrangement):
  for x in range(0, 10):
    for arrangement in arrangements:
      arrangement.randomizeGroups()
    for i in range(0, 40):
      tempArrangements = []
      for arrangement in arrangements:
        for i in range(5):
          arrangement.swapRandomIndividuals()
        arrangement.score = arrangement.calculateScore()
        tempArrangements.append(copy.deepcopy(arrangement))
      result = sorted(tempArrangements, key=lambda x: x.score)
      arrangements = result[-10:]
  print arrangements


#-------------- Make best swap from unhappiest group -----------#
def swapUnhappiest(arrangement):
  previousScoreImprovement = float('inf')
  arrangement.randomizeGroups()
  start = time.time()
  end = time.time()
  while end - start < TIMEOUT and previousScoreImprovement != 0:
    previousScoreImprovement = arrangement.makeBestSwapFromUnhappiestGroup()
    print arrangement
    print previousScoreImprovement
    arrangement.score = arrangement.calculateScore()
  return arrangement

#--------------- Run ----------------------------------#

# Convert CSV
jsonArrangement = csv2json(INPUT_CSV_FILENAME)
# uncomment the following two line to run with sample data
# with open('grouper/sample_data/class40participants.json') as csvFile:
# jsonArrangement = json.dumps(json.load(csvFile))

print jsonArrangement;

arrangements = [Arrangement(jsonString = jsonArrangement) for x in range(NUM_ITERATIONS)]
for arrangement in arrangements:
  arrangement.randomizeGroups()

results = []

for arrangement in arrangements:
  results.append(swapUnhappiest(arrangement))
  results = sorted(results, key = lambda x: x.score)
  print results[-3:]

# # Save to file
for i in range(1, 5):
  arrangement2csv(results[-i], OUTPUT_FOLDER + OUTPUT_FILENAME + '_' + str(i) + '.csv')
