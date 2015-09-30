import copy
import time
from grouper.arrangement import Arrangement
from grouper.group import Group
from grouper.participant import Participant
from grouper.strategy import Strategy
from grouper.arrangement2csv import arrangement2csv

# Constants
OUTPUT_FILENAME = "arrangement"
INPUT_CSV_FILENAME = ""
TIMEOUT = 60 # seconds

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

arrangement = Arrangement('/Users/eihli/Projects/private_sample_data/class.json')

arrangements = [Arrangement('/Users/eihli/Projects/private_sample_data/class.json') for x in range(50)]
for arrangement in arrangements:
  arrangement.randomizeGroups()

results = []

for arrangement in arrangements:
  results.append(swapUnhappiest(arrangement))
  results = sorted(results, key = lambda x: x.score)
  print results[-3:]

# Save to file
for i in range(1, 4):
  arrangement2csv(results[-i], 'arrangement_' + str(i) + '.csv')