from grouper.arrangement import Arrangement
from grouper.group import Group
from grouper.participant import Participant
from grouper.strategy import Strategy

class HackReactorStrategy(Strategy):

  def __init__(self, arrangement):
    return

class HackReactorArrangement(Arrangement):

  def __init__(self, filename = None, numGroups = 1):
    return

class HackReactorParticipant(Participant):

  def __init__(self, name):
    return

class HackReactorGroup(Group):

  def __init__(self):
    return
    
arrangement = HackReactorArrangement('grouper/sample_data/affinities.json')

strategy = HackReactorStrategy(arrangement)
