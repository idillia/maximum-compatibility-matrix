import names
import random
import json
import Participant

class HackReactorGroup(Group):
  def getScore(self):
    score = 0
    for participant1 in self.participants:
      for participant2 in self.participants:
        if participant2 in participant1.likes:
          score += 1


