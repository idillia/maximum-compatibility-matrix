import unittest
from ..participant import Participant
from ..group import Group

class groupTestCase(unittest.TestCase):
  def setUp(self):
    self.group = Group()
    self.participant1 = Participant('eric')
    self.participant2 = Participant('john')
    self.participant3 = Participant('jim')

  def test_group_exists(self):
    self.assertIsInstance(self.group, Group)

  def test_group_can_add_participant(self):
    self.group.addParticipant(self.participant1)
    self.assertEqual(len(self.group.participants), 1)

  def test_group_can_remove_participant(self):
    self.group = Group()
    self.group.addParticipant(self.participant1)
    self.assertEqual(len(self.group.participants), 1)
    self.group.removeParticipant(self.participant1)
    self.assertEqual(len(self.group.participants), 0)

  def test_group_getScore_returns_int(self):
    score = self.group.getScore()
    self.assertIsInstance(score, int)

  # Test the group scoring function.
  # Sum of affinities * weight of affinities
  # Sum of refusals * weight of refusals
  def test_group_getScore_works_with_two_participants_affinities(self):
    self.group.addParticipant(self.participant1)
    self.group.addParticipant(self.participant2)
    self.participant1.addAffinity(self.participant2)
    self.participant2.addAffinity(self.participant1)
    self.assertEqual(self.group.getScore(), 2)

  def test_group_getScore_with_three_participants(self):
    self.group.addParticipant(self.participant1)
    self.group.addParticipant(self.participant2)
    self.group.addParticipant(self.participant3)
    self.participant1.addAffinity(self.participant2)
    self.participant2.addAffinity(self.participant1)
    self.participant3.addTechnicalRefusal(self.participant1)
    self.participant1.addTechnicalRefusal(self.participant3)
    self.participant1.addInterpersonalRefusal(self.participant3)
    self.assertEqual(self.group.getScore(), -298)
