import copy
from grouper.arrangement import Arrangement
from grouper.group import Group
from grouper.participant import Participant
from grouper.strategy import Strategy

arrangement = Arrangement('grouper/sample_data/affinities.json')

strategy = Strategy(arrangement)

# print arrangement

arrangements = [Arrangement('grouper/sample_data/affinities.json') for x in range(10)]
# print arrangements[-3]
# for arrangement in arrangements:
#   for i in range(5):
#     arrangement.swapRandomIndividuals()
#   arrangement.score = arrangement.calculateScore()

# result = map(lambda x: x.calculateScore(), arrangements)
# result = sorted(arrangements, key=lambda x: x.score)
# print result

for i in range(0, 200):
  tempArrangements = []
  for arrangement in arrangements:
    for i in range(3):
      arrangement.swapRandomIndividuals()
      arrangement.score = arrangement.calculateScore()
      tempArrangements.append(copy.deepcopy(arrangement))
  result = sorted(tempArrangements, key=lambda x: x.score)
  arrangements = result[-10:]
print arrangements