# Takes a json formatted arrangement and returns a CSV

# TODO: Remove these hardcoded survey types. Find a better way to get them
# from the arrangement
# TODO: Handle multiple forms of input, not just a json formatted this particular way
def arrangement2csv(arrangement, filename = 'test.csv'):
  surveyTypes = ['affinities', 'technicalRefusals', 'interpersonalRefusals']
  surveyScores = {
    'affinities': '1',
    'technicalRefusals': '-100',
    'interpersonalRefusals': '-100'
  }

  # get a list of participants

  # for each participant as participant1
    # start a new array for this participants affinities
    # for each participant as participant2
      # if participant1 != participant2
        # for each survey type
          # if surveyType[participant1] contains participant2
            # array.push(surveyScore[surveyType])
          # else
            # array.push('')

  result = []
  participants = []
  i = 0
  result.append("Arrangement with score: " + str(arrangement.score) + " with average score " + str(arrangement.score / arrangement.numGroups) + "\n")
  for group in arrangement.groups:
    for participant in group.participants:
      participants.append(participant)
  for group in arrangement.groups:
    result.append("Group " + str(i) + ": Score " + str(group.getScore()))
    i += 1
    for participant1 in group.participants:
      surveyAnswers = [participant1.name]
      for participant2 in participants:
        if participant1 == participant2:
          surveyAnswers.append('N/A')
        else:
          surveyResponse = ''
          for surveyType in range(len(surveyTypes)):
            if participant2 in participant1[surveyTypes[surveyType]]:
              surveyResponse += surveyScores[surveyTypes[surveyType]]
          surveyAnswers.append(surveyResponse)
      result.append(','.join(surveyAnswers))
    result[-1] += "\n"
  # print '\n'.join(result)
  f = open(filename, 'w')
  f.write('\n'.join(result))
  f.close()
  # write result string to file