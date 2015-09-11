from grouper.arrangement import Arrangement
from grouper.group import Group
from grouper.participant import Participant
from grouper.strategy import Strategy

arrangement = Arrangement('grouper/sample_data/affinities.json')

strategy = Strategy(arrangement)

print arrangement


