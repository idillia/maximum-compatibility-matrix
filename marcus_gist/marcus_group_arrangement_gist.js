// https://gist.github.com/marcusphillips/72c519c57c98010a8a7c

var Arrangement = function(people){
  var groupCount =       Math.floor(people.length / 4);
  var groupOfFiveCount = people.length % 4;

  var result = {
    _unassignedPeople: extend({}, people),
    _openGroups: map(range(groupCount), function(index){ return Group(index < groupOfFiveCount ? 5 : 4); }),
    _fullGroups: [],
    desirability: function(){ return TODO(); },
    betterOf: function(contender){ return this.desirability() < contender.desirability() ? contender : this; },
    bestSubarrangement: function(){
      return Arrangement.bestSubarrangements[this.key()] = Arrangement.bestSubarrangements[this.key()] || (
        this.hasConflicts() ? Arrangement.UNWORKABLE :
        !this._unassignedPeople.length ? this :
        reduce(this._unassignedPeople, function(currentBest, person){
          return this.findBestSubarrangementWithPersonPlaced(person).betterOf(currentBest);
        }, Arrangement.UNWORKABLE, this)
      );
    },
    bestSubarrangementWithPersonPlaced: function(person){
      var didTryEmptyGroups = {};
      return reduce(this._openGroups, function(currentBestSubarrangement, group){
        if(!group.memberCount() && didTryEmptyGroups[group.targetSize()]){ return currentBestSubarrangement; }
        didTryEmptyGroups[group.targetSize] = didTryEmptyGroups[group.targetSize] || group.memberCount() === 0;
        var subarrangement = this.copy();
        subarrangement.addToGroup(group.key(), person);
        return subarrangement.bestSubarrangement().betterOf(currentBestSubarrangement);
      }, Arrangement.UNWORKABLE, this);
    },
    addToGroup: function(oldGroupKey, person){
      var group = this._openGroups[groupKey];
      group.add(person);
      var newGroupKey = group.key();
      if(this._openGroups[oldGroupKey].isFull()){
        this._fullGroups[newGroupKey()] = group;
        delete this._openGroups[oldGroupKey];
      }
    }
  };
  return result;
};
Arrangement.bestSubarrangements = {};
Arrangement.UNWORKABLE = Arrangement();
Arrangement.UNWORKABLE.desirability = function(){ return -1; }


var Group = function(targetSize){
  return {
    _targetSize: targetSize,
    _members: {},
    _id: +new Date(),
    id: function(){ return this._id; },
    key: function(){ return this._targetSize + "::" + sort(pluck(this._members, 'name')).concat('::'); },
    compatibility: function(){
      return this._hasConflict ? -1 : this._compatibility;
    },
    addPerson: function(newMember){
      each(this._members, function(member){
        this.compatibility += requestCount(member, newMember);
        this._hasConflict = this._hasConflict || hasConflict(member, newMember);
      };
      this._members[person.name] = person;
    },
    memberCount: function(){ return this._members.length }
  }
}

var people = {
    alice: {technicalRefusals: {}, interpersonalRefusals: {}, affinities: {}},
    bob: {},
    charlie: {}
};

var conflicts = reduce(people, function(memo, person){
  each(person.technicalRefusals.concat(person.interpersonalRefusals), function(refusedPersonsName){
    var conflictKey = JSON.stringify(sort([person.name, refusedPersonsName]));
    memo[conflictKey] = true;
  });
}, {});
console.log(Arrangement(people).findBestSubarrangement();