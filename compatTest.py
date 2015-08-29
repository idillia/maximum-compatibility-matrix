import unittest
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

class cohortTestCase(unittest.TestCase):
  def setUp(self):
    self.cohort = compat.Cohort()

  def test_cohort_exists(self):
    self.assertIsInstance(self.cohort, compat.Cohort)

  def test_cohort_has_list_of_participants(self):
    self.assertIsInstance(self.cohort.participants, list)

  def test_cohort_can_add_participant(self):
    participant = compat.Participant('Eric')
    self.cohort.addParticipant(participant)
    self.assertEqual(self.cohort.participants[0].name, 'Eric')

  def test_cohort_can_be_initiated_with_list_of_names(self):
    participants = ['eric', 'john', 'taylor', 'glenn']
    cohort = compat.Cohort(participants)
    self.assertIsInstance(cohort.participants[0], compat.Participant)
    self.assertEqual(len(cohort.participants), 4)

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

  @unittest.skip("Skipping getscore")
  def test_group_getScore_returns_int(self):
    score = self.group.getScore()
    self.assertIsInstance(score, int)

  @unittest.skip("Skipping getscore")
  def test_group_getScore_works_with_two_participants(self):
    self.group.addParticipant(self.participant1)
    self.group.addParticipant(self.participant2)

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

