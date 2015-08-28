class Participant:

  def __init__(self, name):
    self.name = name
    self.likes = []
    self.dislikes = []

  def like(self, participant):
    self.likes.append(participant)

  def dislike(self, participant):
    self.dislikes.append(participant)

class Cohort:

  def __init__(self):
    self.participants = []

  def addParticipant(self, participant):
    self.participants.append(participant)

class Group:

  def __init__(self):
    self.participants = []

  def addParticipant(self, participant):
    self.participants.append(participant)
    
  def getScore(self):
    return 'false'