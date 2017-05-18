from Fish import Fish

"""
Test Fish
"""

gooFish = Fish("Goo Fish", "GOO")
print "gooFish name is ", gooFish.getName()
print "gooFish makes ", gooFish.getSound(), " noise"

isAre = "is" if Fish.getFishCount() <2 else "are"
print "===There %s %d fish in the pond" % (isAre, Fish.getFishCount())

mooFish = Fish("Moo Fish", "MOO")
print "mooFish makes ", mooFish.getSound(), " noise"
isAre = "is" if Fish.getFishCount() <2 else "are"
print "===There %s %d fish in the pond" % (isAre, Fish.getFishCount())


if (gooFish == mooFish):
   print "Yay, goo is moo!"
else:
   print "Sorry, they are different fish"
