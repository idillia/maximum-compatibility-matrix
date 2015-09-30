import unittest
from ..arrangement import Arrangement
from ..group import Group
from ..participant import Participant
import os

class arrangementTestCase(unittest.TestCase):
  def setUp(self):
    self.arrangement = Arrangement(filename = os.path.abspath(os.path.join('grouper/sample_data/affinities.json')))
    self.arrangement2 = Arrangement()
    self.p1 = Participant("Eric")
    self.p2 = Participant("Sam")
    self.p3 = Participant("Glenn")
    self.p4 = Participant("Taylor")
    self.g1 = Group()
    self.g2 = Group()
    self.arrangement2.addParticipant(self.p1)
    self.arrangement2.addParticipant(self.p2)
    self.arrangement2.addParticipant(self.p3)
    self.arrangement2.addParticipant(self.p4)
    self.arrangement2.addGroup(self.g1)
    self.arrangement2.addGroup(self.g2)



  def test_arrangement_exists(self):
    self.assertIsInstance(self.arrangement, Arrangement)

  def test_arrangement_has_groups(self):
    self.assertIsInstance(self.arrangement.groups, list)

  def test_arrangement_has_participants(self):
    self.assertIsInstance(self.arrangement.participants, list)

  def test_arrangement_add_group(self):
    self.arrangement.addGroup()
    self.assertIsInstance(self.arrangement.groups[0], Group)

  def test_arrangement_get_participant(self):
    self.arrangement.addParticipant(self.p1)
    participant = self.arrangement.getParticipant('Eric')
    self.assertIsInstance(self.arrangement.getParticipant('Eric'), Participant)

  def test_arrangement_add_participant(self):
    self.arrangement.addParticipant(self.p1)
    self.assertIsInstance(self.arrangement.participants[0], Participant)

  def test_arrangement_can_add_participant_to_group(self):
    self.arrangement.groups[0] = self.g1
    self.arrangement.addParticipantToGroup(self.p1, self.g1)
    self.assertIs(self.arrangement.groups[0].participants[0], self.p1)
    self.assertIs(self.p1.group, self.g1)

  def test_arrangement_can_read_from_file(self):
    self.assertEqual(len(self.arrangement.participants), 20)
    self.assertIsInstance(self.arrangement.participants[1], Participant)
    self.assertEqual(self.arrangement.participants[0].name, 'Mary Polster')

  def test_arrangement_can_assign_participants_to_group(self):
    a = Arrangement()
    a.addParticipant(self.p1)
    a.addParticipant(self.p2)
    a.addParticipant(self.p3)
    a.addParticipant(self.p4)
    a.assignParticipantsToGroups(2)
    self.assertEqual(len(a.groups[0].participants), 2)
    self.assertEqual(a.groups[0].participants[0].name, 'Eric')

  def test_arrangement_scoring_function(self):
    self.arrangement.groups = []
    group = Group()
    # TODO: Finish arrangement scoring function/tests

  def test_remove_participant_from_group(self):
    a = Arrangement()
    g = Group()
    a.addGroup(g)
    a.addParticipantToGroup(self.p1, g)
    self.assertEqual(a.groups[0].participants[0].name, 'Eric')
    a.removeParticipantFromGroup(self.p1)
    # Cool way to test the index no longer exists. Trying to access
    # an index out of range raises an IndexError exception.
    with self.assertRaises(IndexError):
        a.groups[0].participants[0]
    # Yeah... len() might work too, and might be more understandable
    # without comments. But this is cool, and these are comments.
    
  # These next tests are something that should be abstracted out into a strategy
  # We want to be able to swap the each person from the unhappiest group
  # into each other group until and keep the "best" arrangement from those
  # swaps.
  def test_get_unhappiest_group(self):
    a = Arrangement()
    a.addGroup()
    a.addGroup()
    p1 = Participant('eric')
    p2 = Participant('john')
    p3 = Participant('sam')
    p4 = Participant('glenn')
    p1.addAffinity(p3)
    p1.addAffinity(p4)
    p2.addTechnicalRefusal(p4)
    a.addParticipantToGroup(p1, a.groups[0])
    a.addParticipantToGroup(p3, a.groups[0])
    a.addParticipantToGroup(p2, a.groups[1])
    a.addParticipantToGroup(p4, a.groups[1])
    self.assertEqual(a.getUnhappiestGroup(), a.groups[1])

  # I think I just found a perfect use case for generators and yield
  # I want to loop over each person in a group, swap that person with each
  # person in each other group, and after each swap, check to see
  # the score of the arrangement. 
  # We don't want the arrangement score checking code inside this function.
  # https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
  def test_makes_best_swap_from_unhappiest_group(self):
    self.p1.addAffinity(self.p2)
    self.p1.addAffinity(self.p4)
    self.p1.addTechnicalRefusal(self.p3)
    self.p2.addAffinity(self.p3)
    self.arrangement2.addParticipantToGroup(self.p1, self.g1)
    self.arrangement2.addParticipantToGroup(self.p3, self.g1)
    self.arrangement2.addParticipantToGroup(self.p2, self.g2)
    self.arrangement2.addParticipantToGroup(self.p4, self.g2)
    self.arrangement2.makeBestSwapFromUnhappiestGroup()
    self.assertEqual(self.arrangement2.calculateScore(), 1)
    self.arrangement2.makeBestSwapFromUnhappiestGroup()
    self.assertEqual(self.arrangement2.calculateScore(), 2)