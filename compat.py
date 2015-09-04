import names
import random
import json


class Participant:

  @staticmethod
  def createRandomParticipant():
    return Participant(names.get_full_name().encode('ascii'))

  def __init__(self, name):
    self.name = name
    self.likes = []
    self.dislikes = []
    self.interpersonalRefusals = []
    self.technicalRefusals = []
    self.affinities = []
    self.group = None
    self.affinityDict = {
      'interpersonal_refusals': self.addInterpersonalRefusal,
      'technical_refusals': self.addTechnicalRefusal,
      'affinities': self.addAffinity
    }

  def __repr__(self):
    result = 'Participant Name: ' + self.name + ':\n'
    result += 'Affinities: \n'
    for affinity in self.affinities:
      result += affinity.name + ' '
    result += '\nInterpersonal Refusals: \n'
    for interpersonalRefusal in self.interpersonalRefusals:
      result += interpersonalRefusal.name + ' ' 
    result += '\nTechnical Refusals: \n'
    for technicalRefusal in self.technicalRefusals:
      result += technicalRefusal.name + ' '
    return result

  def like(self, participant):
    self.likes.append(participant)

  def dislike(self, participant):
    self.dislikes.append(participant)

  def addAffinity(self, participant):
    self.affinities.append(participant)

  def addInterpersonalRefusal(self, participant):
    self.interpersonalRefusals.append(participant)

  def addTechnicalRefusal(self, participant):
    self.technicalRefusals.append(participant)

  def addToGroup(self, group):
    self.group = group

  def removeFromGroup(self):
    self.group = None


class Group:

  def __init__(self):
    self.participants = []

  def addParticipant(self, participant):
    participant.addToGroup(self)
    self.participants.append(participant)

  def removeParticipant(self, participant):
    self.participants.remove(participant)

  def getScore(self):
    score = 0
    for participant1 in self.participants:
      for participant2 in self.participants:
        if participant2 in participant1.likes:
          score += 1
    return score


class Arrangement:
  
  def __init__(self, filename = None, numGroups = 1):
    self.numGroups = numGroups
    self.groups = []
    self.participants = []
    if filename:
      self.readParticipantsFromFile(filename)
    self.strategy = Strategy(self)

  def __repr__(self):
    result = ''
    i = 0
    result += 'Participants:\n'
    for participant in self.participants:
      result += participant.name + '\n'
    for group in self.groups:
      result += "Group " + str(i) + "\n"
      for participant in group.participants:
        result += participant.name + ' '
      result += '\n'
      i += 1
    return result

  def getParticipant(self, name):
    return next(p for p in self.participants if p.name == name)

  def addGroup(self):
    self.groups.append(Group())

  def addParticipant(self, participant):
    self.participants.append(participant)

  def addParticipantToGroup(self, participant, group):
    participant.addToGroup(group)
    group.addParticipant(participant)

  def readParticipantsFromFile(self, filename):
    f = open(filename)
    survey = json.load(f)
    for name in survey['technical_refusals']:
      self.addParticipant(Participant(name))
    # for each participant
    for participant in self.participants:
      # for each survey
      for surveyType in survey:
        # for each person in their list
        for name in survey[surveyType][participant.name]:
          # set their affinity
          print participant.name + ' ' + surveyType + ' ' + name
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


class Strategy:

  def __init__(self, arrangement):
    self.arrangement = arrangement
    self.swapRate = 0.1
    self.maxEVWeight = 1.0
    self.minDiffWeight = 0
    self.allowGroupWithDislike = True
    self.startingPopulation = 10

  def fitness(self):
    score = 0
    for group in self.arrangement.groups:
      score += group.getScore()
    return score