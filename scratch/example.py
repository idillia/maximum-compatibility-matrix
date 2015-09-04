class Participant:
  def __init__(self):
    self.group = None
  
  def addToGroup(group):
    self.group = group
  
  def removeFromGroup(group):
    self.group = None
  
class Group:
  def __init__(self):
    self.participants = []
  
  def addParticipant(participant):
    self.participants.append(participant))
  
  def removeParticipant(participant):
    self.participants.remove(participant)

# I don't want to be able to add a participant to a group without having that
# group also set in the participants group property.

# Right now I have to make 2 to accomplish it.

newParticipant.addToGroup(newGroup)
newGroup.addParticipant(newParticipant)

# This seems bad. What's the best way to handle this?



class Strategy:
  def __init__(self):
    self.mutateRate = 0.1
    self.maximumExpectedValueWeight = 1.0
    self.minimumSacrificialGoatWeight = 0.2
    self.allowGroupWithDislikes = True
    self.startingPopulation = 10
  
  def fitness(self, arrangement):
    score = 0
    for group in arrangement.groups:
      score += group.getScore()
    # Perform other modifications using properties in __init__
    return score