#famousPeople=['platon', 'socrates','jesus']
#friend=famousPeople[0]


#invitationDinner= 'This email pretend to invite you',friend.title(),'to my dinner at 21pm, I would expecting you at my home'
#print(invitationDinner)

#friend=famousPeople[1]


#invitationDinner= 'This email pretend to invite you',friend.title(),'to my dinner at 21pm, I would expecting you at my home'
#print(invitationDinner)

#friend=famousPeople[2]


#invitationDinner= 'This email pretend to invite you',friend.title(),'to my dinner at 21pm, I would expecting you at my home. Well as you may know I got a reservation in a restaurant then I would invite more friends to joint us.'
#print(invitationDinner)

#You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations

famousPeople=['platon', 'socrates','jesus']
del famousPeople[2]
famousPeople.insert(1,'kafka')
friends=famousPeople
print(friends)
friend=famousPeople[1]
invitationDinner= 'This email pretend to invite you',friend.title(),'to my dinner at 21pm, I would expecting you at my home'
print(invitationDinner)
friends.sort()
print(friends)



