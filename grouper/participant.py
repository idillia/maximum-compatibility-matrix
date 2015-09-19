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

  def addInterpersonalRefusal(self, participant):
    self.interpersonalRefusals.append(participant)

  def addTechnicalRefusal(self, participant):
    self.technicalRefusals.append(participant)

  def addToGroup(self, group):
    self.group = group

  def removeFromGroup(self):
    self.group = None