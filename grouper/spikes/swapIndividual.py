import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from grouper import compat
if __name__ == '__main__': 

  arrangement = compat.Arrangement('affinities.json', 5)

  arrangement.assignParticipantsToGroups(5)

  print arrangement

  arrangement.swapRandomIndividuals()

  print arrangement