import unittest
from ..arrangement import Arrangement
from ..group import Group
from ..participant import Participant
import os

class arrangementTestCase(unittest.TestCase):
  def setUp(self):
    self.arrangement = Arrangement()

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
    self.arrangement.addParticipant(Participant('eric'))
    participant = self.arrangement.getParticipant('eric')
    self.assertIsInstance(self.arrangement.getParticipant('eric'), Participant)

  def test_arrangement_add_participant(self):
    participant = Participant('eric')
    self.arrangement.addParticipant(participant)
    self.assertIsInstance(self.arrangement.participants[0], Participant)

  def test_arrangement_can_add_participant_to_group(self):
    participant = Participant('eric')
    group = Group()
    group2 = Group()
    self.arrangement.addParticipantToGroup(participant, group)
    self.assertIs(group.participants[0], participant)
    self.assertIs(participant.group, group)

  def test_arrangement_can_read_from_file(self):
    arrangement = Arrangement(os.path.abspath(os.path.join('grouper/sample_data/affinities.json')))
    self.assertEqual(len(arrangement.participants), 9)
    self.assertIsInstance(arrangement.participants[1], Participant)
    self.assertEqual(arrangement.participants[0].name, 'Luana Chary')

  def test_arrangement_can_assign_participants_to_group(self):
    arrangement = Arrangement(os.path.abspath(os.path.join('grouper/sample_data/affinities.json')))
    print 'Arrangement participants length' + str(len(arrangement.participants))
    print 'Arrangement numGroups' + str(arrangement.numGroups)
    arrangement.assignParticipantsToGroups(4)
    self.assertEqual(len(arrangement.groups[0].participants), 3)
    self.assertEqual(arrangement.groups[0].participants[0].name, 'Luana Chary')