import unittest
from ..participant import Participant
from ..group import Group

class participantTestCase(unittest.TestCase):
  def setUp(self):
    self.participant = Participant('Eric')
    self.friend = Participant('John')
    self.enemy = Participant('Spike')

  def test_participant_name(self):
    self.assertEqual(self.participant.name, 'Eric')

  def test_participant_interpersonal_refusals(self):
    self.assertIsInstance(self.participant.interpersonalRefusals, list)

  def test_participant_technical_refusals(self):
    self.assertIsInstance(self.participant.technicalRefusals, list)

  def test_add_affinity(self):
    self.participant.addAffinity(self.friend)
    self.assertEqual(self.friend, self.participant.affinities[0])
    
  def test_add_interpersonal_refusal(self):
    self.participant.addInterpersonalRefusal(self.enemy)
    self.assertEqual(self.enemy, self.participant.interpersonalRefusals[0])

  def test_add_technical_refusal(self):
    self.participant.addTechnicalRefusal(self.enemy)
    self.assertEqual(self.enemy, self.participant.technicalRefusals[0])

  def test_participant_can_be_added_to_group(self):
    group = Group()
    self.participant.addToGroup(group)
    self.assertIs(self.participant.group, group)

  def test_participant_can_be_removed_from_group(self):
    group = Group()
    self.participant.addToGroup(group)
    self.assertEqual(group, self.participant.group)
    self.participant.removeFromGroup()
    self.assertEqual(self.participant.group, None)

  def test_paricipant_create_random(self):
    participant1 = Participant.createRandomParticipant()
    participant2 = Participant.createRandomParticipant()
    self.assertIsInstance(participant1.name, str)
    self.assertIsInstance(participant2.name, str)
    self.assertNotEqual(participant1.name, participant2.name)