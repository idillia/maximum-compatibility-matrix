import json
import random
from strategy import Strategy
from participant import Participant
from group import Group
NUM_INDIVIDUALS_PER_GROUP = 4

class Arrangement:
  
  def __init__(self, filename = None):
    self.groups = []
    self.participants = []
    if (filename):
      self.readParticipantsFromFile(filename)
    self.numGroups = len(self.participants) / NUM_INDIVIDUALS_PER_GROUP
    self.assignParticipantsToGroups(self.numGroups)
    self.strategy = Strategy(self)
    self.score = None

  def __repr__(self):
    result = ''
    i = 0
    result += "Arrangement with Score: " + str(self.score) + '\n'
    result += 'Participants:\n'
    for participant in self.participants:
      result += participant.name + ', '
    result = result[:-2] + '\nGroups:\n' 
    for group in self.groups:
      result += "Group " + str(i) + "\n"
      result += group.__repr__() + '\n'
      i += 1
    result += '\n'
    return result

  def getParticipant(self, name):
    return next(p for p in self.participants if p.name == name)

  def addGroup(self, group = None):
    #TODO: Handle passing in a group with participants.
    # Add participants to list. Etc...
    group = group or Group()
    self.groups.append(group)

  def addParticipant(self, participant):
    self.participants.append(participant)

  def addParticipantToGroup(self, participant, group):
    participant.addToGroup(group)
    group.addParticipant(participant)
    group.getScore()

  # TODO: Test
  def removeParticipantFromGroup(self, participant):
    group = participant.group
    participant.removeFromGroup()
    group.removeParticipant(participant)
    group.getScore()

  def calculateScore(self):
    return sum(group.getScore() for group in self.groups)

  def readParticipantsFromFile(self, filename):
    f = open(filename)
    survey = json.load(f)
    for name in survey['technical_refusals']:
      self.addParticipant(Participant(name))
    for participant in self.participants:
      for surveyType in survey:
        for name in survey[surveyType][participant.name]:
          # set their affinity
          # print participant.name + ' ' + surveyType + ' ' + name
          participant.affinityDict[surveyType](self.getParticipant(name))

  def assignParticipantsToGroups(self, numGroups):
    for i in range(numGroups):
      self.addGroup()
    for i in range(len(self.participants)):
      self.addParticipantToGroup(self.participants[i], self.groups[i % numGroups])

  def randomizeGroups(self):
    self.groups = []
    random.shuffle(self.participants)
    for i in range(self.numGroups):
      self.addGroup()
    for i in range(len(self.participants)):
      self.addParticipantToGroup(self.participants[i], self.groups[i % self.numGroups])

  def swapRandomIndividuals(self):
    numGroups = self.numGroups
    if numGroups == 1:
      raise ValueError('Number of groups in arrangement must be greater than 1 for mutating.')

    firstGroupIndex = random.randint(0, numGroups-1)
    secondGroupIndex = random.randint(0, numGroups-1)
    while secondGroupIndex == firstGroupIndex:
      secondGroupIndex = random.randint(0, numGroups-1)

    firstGroup = self.groups[firstGroupIndex]
    secondGroup = self.groups[secondGroupIndex]

    firstIndividualIndex = random.randint(0, len(firstGroup.participants) - 1)
    secondIndividualIndex = random.randint(0, len(secondGroup.participants) - 1)

    firstIndividual = self.groups[firstGroupIndex].participants[firstIndividualIndex]
    self.groups[firstGroupIndex].participants[firstIndividualIndex] = self.groups[secondGroupIndex].participants[secondIndividualIndex]
    self.groups[secondGroupIndex].participants[secondIndividualIndex] = firstIndividual

  def getUnhappiestGroup(self):
    return reduce(lambda g, a: g if g.getScore() < a.getScore() else a, self.groups)

  # TODO: Test
  def swapIndividuals(self, a, b):
    bGroup = b.group
    aGroup = a.group
    self.removeParticipantFromGroup(b)
    self.addParticipantToGroup(a, bGroup)
    self.addParticipantToGroup(b, aGroup)

  def makeBestSwap(self):
    for i in self.numGroups:
      for p1 in self.groups[i]:
        for j in self.numGroups:
          if not i == j:
            for p2 in self.groups[j]:
              self.swapIndividuals(p1, p2)

  def makeBestSwapFromUnhappiestGroup(self):
    unhappiestGroup = self.getUnhappiestGroup()
    print unhappiestGroup
    return unhappiestGroup