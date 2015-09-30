class Group:

  def __init__(self):
    self.participants = []
    self.score = None

  def __repr__(self):
    result = ''
    i = 0
    # TODO: Removed hardcoded getWeightedScore numParticipants
    result += "Group Score: " + str(self.getScore()) + '\n'
    for p in self.participants:
      result += p.name + ', '
    result = result[:-2] + '\n'
    return result

  def addParticipant(self, participant):
    participant.addToGroup(self)
    self.participants.append(participant)

  def removeParticipant(self, participant):
    self.participants.remove(participant)

  # TODO:
  # Add weights. Right now, every affinity/refusal is just +- 1 point.
  def getScore(self):
    score = 0
    for participant1 in self.participants:
      for participant2 in self.participants:
        if participant1 != participant2:
          if participant2 in participant1.affinities:
            score += 1
          if participant2 in participant1.technicalRefusals:
            score -= 100
          if participant2 in participant1.interpersonalRefusals:
            score -= 100
    self.score = score
    return self.score


  # def getWeightedScore(self, numParticipants):
  #   score = 0
  #   for participant1 in self.participants:
  #     for participant2 in self.participants:
  #       if participant1 != participant2:
  #         if participant2 in participant1.affinities:
  #           score += 1.0 - (1.0 * participant1.numAffinities / numParticipants)
  #         if participant2 in participant1.technicalRefusals:
  #           score -= 100
  #         if participant2 in participant1.interpersonalRefusals:
  #           score -= 100
  #         if participant2 not in participant1.affinities and participant2 not in participant1.technicalRefusals and participant2 not in participant1.interpersonalRefusals:
  #           score += -1 * (1.0 * participant1.numAffinities / numParticipants) + 1.0 * participant1.numTechnicalAndInterpersonalRefusals / numParticipants
  #   return score
