# Takes a json formatted arrangement and returns a CSV

# TODO: Remove these hardcoded survey types. Find a better way to get them
# from the arrangement
surveyTypes = ['affinities', 'technicalRefusals', 'interpersonalRefusals']
surveyScores = {
  'affinities': '1',
  'technicalRefusals': '-100',
  'interpersonalRefusals': '-100'
}
# TODO: Handle multiple forms of input, not just a json formatted this particular way
def arrangement2csv(arrangement):
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
  # get a list of participants in order of groups
  participants = []
  for group in arrangement.groups:
    for participant in group.participants:
      participants.append(participant)
  # for each group in arrangement.groups
  for group in arrangement.groups:
    # for each participant in group.participants as participant1
    for participant1 in group.participants:
      # start a new array for this participants affinities
      surveyAnswers = [participant1.name]
      # for each participant in all participants as participant2
      for participant2 in participants:
        # if participant1 != participant2
        if participant1 == participant2:
          surveyAnswers.append('N/A')
        else:
          # for each survey type
          surveyResponse = ''
          for surveyType in range(len(surveyTypes)):
            # if surveyType[participant1] contains participant2
            if participant2 in participant1[surveyTypes[surveyType]]:
              print participant2.name + ' is in ' + participant1.name + "'s " + surveyTypes[surveyType]
              # array.push(surveyScore[surveyType])
              surveyResponse += surveyScores[surveyTypes[surveyType]]
              print surveyResponse
          surveyAnswers.append(surveyResponse)

      # join array with commas
      print surveyAnswers
      result.append(','.join(surveyAnswers))
      # append to result string with newline at end
  print '\n'.join(result)
  f = open('test.csv', 'w')
  f.write('\n'.join(result))
  f.close()
  # write result string to file