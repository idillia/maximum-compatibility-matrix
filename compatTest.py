import unittest
import json
import compat

class participantTestCase(unittest.TestCase):
  def setUp(self):
    self.participant = compat.Participant('Eric')
    self.friend = compat.Participant('John')
    self.enemy = compat.Participant('Spike')

  def test_participant_name(self):
    self.assertEqual(self.participant.name, 'Eric')

  def test_participant_likes(self):
    self.assertIsInstance(self.participant.likes, list)

  def test_participant_dislikes(self):
    self.assertIsInstance(self.participant.dislikes, list)

  def test_participant_add_likes(self):
    self.participant.like(self.friend)
    self.assertEqual(len(self.participant.likes), 1)
    self.assertIsInstance(self.participant.likes[0], compat.Participant)

  def test_participant_add_dislikes(self):
    self.participant.dislike(self.enemy)
    self.assertEqual(len(self.participant.dislikes), 1)
    self.assertIsInstance(self.participant.dislikes[0], compat.Participant)

  def test_participant_can_be_added_to_group(self):
    group = compat.Group()
    self.participant.addToGroup(group)
    self.assertIs(self.participant.group, group)

  def test_participant_can_be_removed_from_group(self):
    group = compat.Group()
    self.participant.addToGroup(group)
    self.assertEqual(group, self.participant.group)
    self.participant.removeFromGroup()
    self.assertEqual(self.participant.group, None)

  def test_paricipant_create_random(self):
    participant1 = compat.Participant.createRandomParticipant()
    participant2 = compat.Participant.createRandomParticipant()
    self.assertIsInstance(participant1.name, str)
    self.assertIsInstance(participant2.name, str)
    self.assertNotEqual(participant1.name, participant2.name)

class groupTestCase(unittest.TestCase):
  def setUp(self):
    self.group = compat.Group()
    self.participant1 = compat.Participant('eric')
    self.participant2 = compat.Participant('john')

  def test_group_exists(self):
    self.assertIsInstance(self.group, compat.Group)

  def test_group_can_add_participant(self):
    self.group.addParticipant(self.participant1)
    self.assertEqual(len(self.group.participants), 1)

  def test_group_can_remove_participant(self):
    self.group = compat.Group()
    self.group.addParticipant(self.participant1)
    self.assertEqual(len(self.group.participants), 1)
    self.group.removeParticipant(self.participant1)
    self.assertEqual(len(self.group.participants), 0)

  def test_group_getScore_returns_int(self):
    score = self.group.getScore()
    self.assertIsInstance(score, int)

  def test_group_getScore_works_with_two_participants(self):
    self.group.addParticipant(self.participant1)
    self.group.addParticipant(self.participant2)
    self.participant1.like(self.participant2)
    self.assertEqual(self.group.getScore(), 1)
    self.participant2.like(self.participant1)
    self.assertEqual(self.group.getScore(), 2)

class arrangementTestCase(unittest.TestCase):
  def setUp(self):
    self.arrangement = compat.Arrangement()

  def test_arrangement_exists(self):
    self.assertIsInstance(self.arrangement, compat.Arrangement)

  def test_arrangement_has_groups(self):
    self.assertIsInstance(self.arrangement.groups, list)

  def test_arrangement_has_participants(self):
    self.assertIsInstance(self.arrangement.participants, list)

  def test_arrangement_add_group(self):
    self.arrangement.addGroup()
    self.assertIsInstance(self.arrangement.groups[0], compat.Group)

  def test_arrangement_get_participant(self):
    self.arrangement.addParticipant(compat.Participant('eric'))
    participant = self.arrangement.getParticipant('eric')
    self.assertIsInstance(self.arrangement.getParticipant('eric'), compat.Participant)

  def test_arrangement_add_participant(self):
    participant = compat.Participant('eric')
    self.arrangement.addParticipant(participant)
    self.assertIsInstance(self.arrangement.participants[0], compat.Participant)

  def test_arrangement_can_add_participant_to_group(self):
    participant = compat.Participant('eric')
    group = compat.Group()
    group2 = compat.Group()
    self.arrangement.addParticipantToGroup(participant, group)
    self.assertIs(group.participants[0], participant)
    self.assertIs(participant.group, group)

  def test_arrangement_can_read_from_file(self):
    arrangement = compat.Arrangement('sampleData.json')
    self.assertEqual(len(arrangement.participants), 9)
    self.assertIsInstance(arrangement.participants[1], compat.Participant)
    self.assertEqual(arrangement.participants[0].name, 'Luana Chary')

  def test_arrangement_can_assign_participants_to_group(self):
    arrangement = compat.Arrangement('sampleData.json')
    arrangement.assignParticipantsToGroups(3)
    self.assertEqual(len(arrangement.groups[0].participants), 3)
    self.assertEqual(arrangement.groups[0].participants[0].name, 'Luana Chary')
    # print arrangement

class strategyTestCase(unittest.TestCase):
  def setUp(self):
    self.arrangement = compat.Arrangement()
    self.strategy = compat.Strategy(self.arrangement)

  def test_strategy_exists(self):
    self.assertIsInstance(self.strategy, compat.Strategy)

  def test_strategy_fitness_returns_int(self):
    self.assertIsInstance(self.strategy.fitness(), int)