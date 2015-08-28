import names

class Participant:

  @staticmethod
  def createRandomParticipant():
    return Participant(names.get_full_name().encode('ascii'))

  def __init__(self, name):
    self.name = name
    self.likes = []
    self.dislikes = []
    self.group = None

  def like(self, participant):
    self.likes.append(participant)

  def dislike(self, participant):
    self.dislikes.append(participant)

  def addToGroup(self, group):
    self.group = group

class Cohort:

  def __init__(self):
    self.participants = []
    self.groups = []

  def addGroup(self, group):
    self.groups.append(group)

  def addParticipant(self, participant):
    self.participants.append(participant)

  def addParticipantToGroup(self, participant, group):
    participant.addToGroup(group)
    group.addParticipant(participant)

class Group:

  def __init__(self):
    self.participants = []

  def addParticipant(self, participant):
    participant.addToGroup(self)
    self.participants.append(participant)

  def getScore(self):
    return 'false'

class Arrangement:
  
  def __init__(self):
    self.groups = []