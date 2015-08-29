import random
import compat
import math

# Create a cohort.

cohort = compat.Cohort()

print cohort

# Create some random participants
for x in range(0, 40):
  cohort.addParticipant(compat.Participant.createRandomParticipant())
# for participant in cohort.participants:
  # print participant.name

# Create an arrangement
arrangement = compat.Arrangement()
arrangement.participants = cohort.participants

# Create the number of groups so that we have 4 participants per group.
numGroups = int(math.floor(len(cohort.participants) / 4))
# print numGroups
for i in range(numGroups):
  arrangement.addGroup()

# Assign those participants to groups.
for i in range(len(cohort.participants)):
  arrangement.addParticipantToGroup(cohort.participants[i], arrangement.groups[i % 10])

# Check to make sure we have 4 participants per group
# for group in arrangement.groups:
#   for participant in group.participants:
#     print group
#     print participant.name

# Add random likes and dislikes for each participant.

for participant1 in cohort.participants:
  for participant2 in cohort.participants:
    if participant1 == participant2:
      continue
    if random.random() > 0.8:
      participant1.like(participant2)
    elif random.random() < 0.1:
      participant1.dislike(participant2)

for i in range(10):
  participant = arrangement.participants[i]
  print participant.name
  print str(map(lambda p: p.name, participant.likes))
  print str(map(lambda p: p.name, participant.dislikes))
  # print arrangement.participants[i].name + " " + ', '.join(arrangement.participants[i].likes) + " " + ', '.join(arrangement.participants[i].dislikes)