# A Participant is a member of a group. The participant
# has a list of other participants they like and dislike
class Participant:
  def __init__(self):
    self.group = None
    self.likes = []
    self.dislikes = []
  
  def addToGroup(group):
    self.group = group
  
  def removeFromGroup(group):
    self.group = None

  def likes(self, participant):
    self.likes.append(participant)

  def dislikes(self, participant):
    self.dislikes.append(participant)

# A Group is a list of participants.
class Group:
  def __init__(self):
    self.participants = []
  
  def addParticipant(participant):
    self.participants.append(participant))
  
  def removeParticipant(participant):
    self.participants.remove(participant)

# I don't want to be able to add a participant to a group without having that
# group also set in the participants group property.

# Right now I have to make 2 calls to accomplish it.

Cohort
  cohort.addParticipantToGroup
    newParticipant.addToGroup(newGroup)
    newGroup.addParticipant(newParticipant)
    

# This seems bad. What's the best way to handle this?
# I want to make sure it is impossible for the two
# to be out of sync.



# An Arrangement is a list of groups with participants.
class Arrangement:
  def __init__(self):
    self.participants = []
    self.groups = []

  def addGroup(self, group):
    self.groups.append(group)

  def addParticipant(self, participant):
    self.participants.append(participant)

# A Strategy is a way to calculate the compatibility
# score of an Arrangement.
class Strategy:
  def __init__(self, arrangement):
    self.arrangement = arrangement
    self.mutateRate = 0.1
    self.maximumExpectedValueWeight = 1.0
    self.minimumSacrificialGoatWeight = 0.2
    self.allowGroupWithDislikes = True
    self.startingPopulation = 10
  
  def score(self, arrangement):
    score = 0
    for group in arrangement.groups:
      score += group.getScore()
    # Perform other modifications using properties in __init__
    return score

# Different situations could call for different strategies.
# What's the best way to decouple Strategies and Arrangements
# so that the strategy can work with different arrangements.
# For example:
# What if the participants are Flowers and we want
# to create 5 groups of flowers that are most similar in color
# while minimizing the height difference between the flowers
# of a group and adding some weight to flowers that smell
# similarly.


# So now where do we go?
myArrangement.score(Strategy(param1, param2, param3))
# or
myStrategy.score(myArrangement)

