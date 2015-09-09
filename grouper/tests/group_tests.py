import unittest
from ..participant import Participant
from ..group import Group

class groupTestCase(unittest.TestCase):
  def setUp(self):
    self.group = Group()
    self.participant1 = Participant('eric')
    self.participant2 = Participant('john')

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

  @unittest.skip("Not working. Job for child class")
  def test_group_getScore_works_with_two_participants(self):
    self.group.addParticipant(self.participant1)
    self.group.addParticipant(self.participant2)
    self.participant1.like(self.participant2)
    self.assertEqual(self.group.getScore(), 1)
    self.participant2.like(self.participant1)
    self.assertEqual(self.group.getScore(), 2)
