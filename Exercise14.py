from sys import argv

script, user_name = argv
prompt = '> '

print "Hello this is my %s and its called %s"  % (script, user_name)
print "Id like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s" % user_name
computer = raw_input(prompt)

print """
okay, you said you like me %s.
You live in %s.
And you have this computer %s.
""" % (likes, lives, computer)
