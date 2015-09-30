import names

class Participant:

  @staticmethod
  def createRandomParticipant():
    return Participant(names.get_full_name().encode('ascii'))

  def __init__(self, name):
    self.name = name
    self.interpersonalRefusals = []
    self.technicalRefusals = []
    self.affinities = []
    self.group = None
    self.affinityDict = {
      'interpersonal_refusals': self.addInterpersonalRefusal,
      'technical_refusals': self.addTechnicalRefusal,
      'affinities': self.addAffinity
    }
    self.numAffinities = 0
    self.numTechnicalRefusals = 0
    self.numInterpersonalRefusals = 0
    self.numTechnicalAndInterpersonalRefusals = 0

  def __getitem__(self, i):
    return getattr(self, i)

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

  def addAffinity(self, participant):
    self.affinities.append(participant)
    self.numAffinities += 1

  def addInterpersonalRefusal(self, participant):
    self.interpersonalRefusals.append(participant)
    self.numInterpersonalRefusals += 1
    if participant not in self.technicalRefusals:
      self.numTechnicalAndInterpersonalRefusals += 1

  def addTechnicalRefusal(self, participant):
    self.technicalRefusals.append(participant)
    self.numTechnicalRefusals += 1
    if participant not in self.interpersonalRefusals:
      self.numTechnicalAndInterpersonalRefusals += 1

  def addToGroup(self, group):
    self.group = group

  def removeFromGroup(self):
    self.group = None