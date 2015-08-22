import unittest
import compat

class participantTestCase(unittest.TestCase):
  def setUp(self):
    self.participant = compat.Participant('Eric')

  def test_participant_name(self):
    self.assertEqual(self.participant.name, 'Eric')

  def test_participant_likes(self):
    self.assertIsInstance(self.participant.likes, list)

  def test_participant_dislikes(self):
    self.assertIsInstance(self.participant.dislikes, list)

  def test_participant_add_likes(self):
    friend = compat.Participant('John')
    self.participant.like(friend)
    self.assertEqual(len(self.participant.likes), 1)
    self.assertIsInstance(self.participant.likes[0], compat.Participant)
