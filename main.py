import copy
from grouper.arrangement import Arrangement
from grouper.group import Group
from grouper.participant import Participant
from grouper.strategy import Strategy
from grouper.arrangement2csv import arrangement2csv

arrangement = Arrangement('/Users/eihli/Projects/private_sample_data/class.json')

strategy = Strategy(arrangement)

arrangements = [Arrangement('/Users/eihli/Projects/private_sample_data/class.json') for x in range(10)]
for arrangement in arrangements:
  arrangement.randomizeGroups()

# ------------- Genetic Algorithm. Random Swaps -------------#
# for x in range(0, 10):
#   for arrangement in arrangements:
#     arrangement.randomizeGroups()
#   for i in range(0, 40):
#     tempArrangements = []
#     for arrangement in arrangements:
#       for i in range(5):
#         arrangement.swapRandomIndividuals()
#       arrangement.score = arrangement.calculateScore()
#       tempArrangements.append(copy.deepcopy(arrangement))
#     result = sorted(tempArrangements, key=lambda x: x.score)
#     arrangements = result[-10:]
# print arrangements


#-------------- Make best swap from unhappiest group -----------#
for arrangement in arrangements[0:3]:
  arrangement.randomizeGroups()
  for i in range(0, 10):
    arrangement.makeBestSwapFromUnhappiestGroup()
    print arrangement
  arrangement.score = arrangement.calculateScore()
result = sorted(arrangements, key = lambda x: x.score)
print result

for i in range(1, 4):
  arrangement2csv(result[-i], 'arrangement_' + str(i) + '.csv')