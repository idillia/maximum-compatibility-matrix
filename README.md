#Optimal Grouping with Grouper

##Current State

###Requirements

- `pip install names` - Requires `names` to generate random sample data.

###CSV Format
1. E = Affinity
1. I = Interpersonal Refusal
1. T = Technical Refusal
1. First row should be header with individual's names.
1. First column should be transpose of first row.

###Running The Algorithm
- Open main.py in your editor and set your constants
- Run ``python main.py``
- main.py will convert the CSV to a JSON format that the algorithm can use.
- Scoring is currently hardcoded into group.py, +1 for affinity and -100 for refusals.
- The last 3 groups logged to the console will be the most optimal solutions.
- Those groups will also be written to files defined in your constants.

##The Idea

###Classes

####Individual (Currently named Participant - TODO: Rename/Refactor)

Individuals have properties by which they are grouped.

####Groups

Groups of individuals. This class has a scoring function (Strategy) which returns the "fit" of the individuals inside a group.

####Arrangements

Groups of groups. This class also has a scoring function (Strategy) which returns the "fit" of all of the groups.

####Strategy

*Not yet implemented*

Has knowledge of a class (Group, Arrangement). Registered by the class so that the class knows how to score and/or run. (We might need different Strategy classes for Groups and Arrangements.)

1. Design an individual
  1. It should have properties by which its "fit" with other individuals in a group can be evaluated.
  1. It should have a property listing the properties by which it should be graded. Other classes will be looking to this property.
1. Design a group.
  1. DEV NOTE: Could this be written so that you could just pass in an individual and have the group automatically get all of the information it needs? Can we write this so that we don't need to edit any Group code no matter what our Individuals look like?
  1. It will have a list of individuals.
  1. It will have a scoring function.

####TODO: Finish the above

##Meanwhile...

1. Define constants so values/weights can be easily modified.
1. Define constants for filenames.
1. Decouple