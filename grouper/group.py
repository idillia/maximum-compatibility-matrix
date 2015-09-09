class Group:

  def __init__(self):
    self.participants = []

  def addParticipant(self, participant):
    participant.addToGroup(self)
    self.participants.append(participant)

  def removeParticipant(self, participant):
    self.participants.remove(participant)

  def getScore(self):
    return 0;
