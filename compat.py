class Participant:

  def __init__(self, name):
    self.name = name
    self.likes = []
    self.dislikes = []

  def like(self, participant):
    self.likes.append(participant)
