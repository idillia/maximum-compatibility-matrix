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
        if participant1 != participant2:
          if participant2 in participant1.affinities:
            score += 1
          if participant2 in participant1.technicalRefusals:
            score -= 1
          if participant2 in participant1.interpersonalRefusals:
            score -= 1
    return score
