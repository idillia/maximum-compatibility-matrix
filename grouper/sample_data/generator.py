import random
import json
from ..arrangement import Arrangement
from ..participant import Participant
import math

# Create a arrangement.

arrangement = Arrangement()

# Create some random participants
for x in range(0, 40):
  arrangement.addParticipant(Participant.createRandomParticipant())
# for participant in arrangement.participants:
#   print participant.name

# Create the number of groups so that we have 4 participants per group.
numGroups = int(math.floor(len(arrangement.participants) / 4))
# print numGroups
for i in range(numGroups):
  arrangement.addGroup()

# Assign those participants to groups.
for i in range(len(arrangement.participants)):
  arrangement.addParticipantToGroup(arrangement.participants[i], arrangement.groups[i % numGroups])

# Check to make sure we have 4 participants per group
# for group in arrangement.groups:
#   for participant in group.participants:
#     print group
#     print participant.name

# Add random likes and dislikes for each participant.

for participant1 in arrangement.participants:
  for participant2 in arrangement.participants:
    if participant1 == participant2:
      continue
    if random.random() > 0.8:
      participant1.like(participant2)
    elif random.random() < 0.1:
      participant1.addInterpersonalRefusal(participant2)
    elif random.random() < 0.1:
      participant1.addTechnicalRefusal(participant2)
participants = []

result = {}
result['affinities'] = {}
result['interpersonal_refusals'] = {}
result['technical_refusals'] = {}

for i in range(len(arrangement.participants)):
  participant = arrangement.participants[i]
  # print participant.name
  # print str(map(lambda p: p.name, participant.likes))
  # print str(map(lambda p: p.name, participant.dislikes))
  result['affinities'][participant.name] = map(lambda p: p.name, participant.likes)
  result['interpersonal_refusals'][participant.name] = map(lambda p: p.name, participant.interpersonalRefusals)
  result['technical_refusals'][participant.name] = map(lambda p: p.name, participant.technicalRefusals)
  # participants[participant.name] = {}
  # participants[participant.name]['likes'] = map(lambda p: p.name, participant.likes)
  # participants[participant.name]['dislikes'] = map(lambda p: p.name, participant.dislikes)
  # print arrangement.participants[i].name + " " + ', '.join(arrangement.participants[i].likes) + " " + ', '.join(arrangement.participants[i].dislikes)
# print participants

print json.dumps(result, indent=2, separators=(',', ': '))
f = open('class.json', 'w')
f.write(json.dumps(result, indent=2, separators=(',', ': ')))

# arrangement = Arrangement()
# arrangement.readParticipantsFromFile('sampleData.json')
# arrangement.createGroups(3)
# arrangement.assignParticipantsToGroups()
# arrangement.setStrategy(Strategy())
# arrangement.getScore()

# compatSolver.init(Arrangement, 10, Strategy, dataSet)