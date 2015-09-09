class Strategy:

  def __init__(self, arrangement):
    self.arrangement = arrangement
    self.swapRate = 0.1
    self.maxEVWeight = 1.0
    self.minDiffWeight = 0
    self.allowGroupWithDislike = True
    self.startingPopulation = 10

  def fitness(self):
    score = 0
    for group in self.arrangement.groups:
      score += group.getScore()
    return score