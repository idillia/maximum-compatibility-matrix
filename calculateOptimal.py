import grouper
import grouper.participant
import random

def calculateGroupScore(group):
  score = 0
  for participant1 in group.participants:
    for participant2 in group.participants:
      if participant2 in participant1.affinities:
        score += 1
  return score

arrangements = []

# Generate 10 random lists and push them to arrangements
for i in range(10):
  arrangement = compat.Arrangement('affinities.json', 5)
  arrangement.randomizeGroups()
  arrangements.append(arrangement)

# For each arrangement
arrangementScores = []
for arrangement in arrangements:
  sumGroupScores = 0
  # For each group in the arrangement
  for group in arrangement.groups:
    groupScore = calculateGroupScore(group)
    # Calculate score of group
    sumGroupScores += groupScore
    # sumGroupScores += group.getScore()
  arrangementScores.append(sumGroupScores)

print arrangementScores
  # Sum the scores of the groups
  # Calculate the sum of the difference of the scores of the groups.
  # Calculate the score of the arrangement (sumOfGroups * weight) - (sumOfSquaresOfDifferencesBetweenGroups * weight)
  # ... or something like that

# Rank the arrangments by score.
# Take the top ... 5? arrangements and make 5 swaps.
# Goto 15 and repeat.

def generateRandomArrangement(filename, numGroups):
  arrangement = compat.Arrangement('affinities.json', 5)
  arrangement.assignParticipantsToGroups(5)

def mutateArrangements(arrangements, numMutations):
  return

def mutateArrangement(arrangement, numMutations):
  return

arrangement = compat.Arrangement('affinities.json', 5)


arrangement.assignParticipantsToGroups(5)

print 'Participants: ' + str(map(lambda p: p.name, arrangement.groups[0].participants))
print 'Participant 1 affinities: ' + str(map(lambda p: p.name, arrangement.groups[0].participants[0].affinities))
print 'Participant 2 affinities: ' + str(map(lambda p: p.name, arrangement.groups[0].participants[1].affinities))
print 'Participant 3 affinities: ' + str(map(lambda p: p.name, arrangement.groups[0].participants[2].affinities))
print 'Participant 4 affinities: ' + str(map(lambda p: p.name, arrangement.groups[0].participants[3].affinities))
print 'Group 0 score: ' + str(calculateGroupScore(arrangement.groups[0]))

print 'Scores of the 10 random arrangements: ' + str(arrangementScores)

# Grouper.strategy = myStrategy;
# Grouper.arrangement = myArrangement
# Grouper.groupScoringFunction = groupScoringFunction
