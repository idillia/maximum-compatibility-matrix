import json
import math
import random
from strategy import Strategy
from participant import Participant
from group import Group
NUM_INDIVIDUALS_PER_GROUP = 4

class Arrangement:
  
  def __init__(self, filename = None, jsonString = None):
    self.groups = []
    self.participants = []
    if (filename):
      self.readParticipantsFromFile(filename)
    if (jsonString):
      self.loadParticipantsFromJson(jsonString)
    self.numGroups = int(math.ceil(1.0 * len(self.participants) / NUM_INDIVIDUALS_PER_GROUP))
    self.assignParticipantsToGroups(self.numGroups)
    self.strategy = Strategy(self)
    self.score = None

  def __repr__(self):
    result = ''
    averageGroupScore = reduce(lambda x, y: x + y.getScore(), self.groups, 0) / self.numGroups
    print averageGroupScore
    i = 0
    result += "Arrangement with Score: " + str(self.score) + " "
    result += "with average score: " + str(averageGroupScore) + '\n'
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

  def loadParticipantsFromJson(self, jsonString):
    survey = json.loads(jsonString)
    print survey
    for name in survey['technical_refusals']:
      self.addParticipant(Participant(name))
    for participant in self.participants:
      for surveyType in survey:
        for name in survey[surveyType][participant.name]:
          # set their affinity
          # print participant.name + ' ' + surveyType + ' ' + name
          participant.affinityDict[surveyType](self.getParticipant(name))


  def assignParticipantsToGroups(self, numGroups):
    for i in range(self.numGroups):
      self.addGroup()
    print "Num groups: " + str(self.numGroups)
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
    self.removeParticipantFromGroup(a)
    self.addParticipantToGroup(a, bGroup)
    self.addParticipantToGroup(b, aGroup)

  def makeBestSwap(self):
    for i in self.numGroups:
      for p1 in self.groups[i]:
        for j in self.numGroups:
          if not i == j:
            for p2 in self.groups[j]:
              self.swapIndividuals(p1, p2)

  # This should be pulled out into a subclass or Arrangement Strategy or something.
  def makeBestSwapFromUnhappiestGroup(self):
    bestGain = 0
    bestSwap = (None, None)
    unhappiestGroup = self.getUnhappiestGroup()
    for participant1 in unhappiestGroup.participants:
      for group in self.groups:
        if group != unhappiestGroup:
          for participant2 in group.participants:
            oldScore = self.calculateScore()
            self.swapIndividuals(participant1, participant2)
            newScore = self.calculateScore()
            if newScore >= oldScore:
              bestGain = newScore - oldScore
              bestSwap = (participant1, participant2)
            self.swapIndividuals(participant1, participant2)
    # Only swap if we there is a better swap to make.
    if bestSwap[0] != None:
      self.swapIndividuals(bestSwap[0], bestSwap[1])
    return bestGain