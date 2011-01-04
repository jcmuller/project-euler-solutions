ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards = lambda hand: zip(*[[ranks.index(card[0:-1]), card[-1]] for card in hand])

# Note that we're going to be scanning through each hand combination in descending order. Each lambda
# returns a tuple containing a boolean is the hand applies along with a list of ranks that are considered
# high cards.
hands = [ lambda hand: # Royal Flush - Return 'A' as high card.
             (len(set(hand[1]))==1 and set(hand[0]) == set(range(ranks.index('T'), ranks.index('T')+5)),
             [ranks[-1]]),
          lambda hand: # Straight Flush - Return highest card in hand as high card
             (len(set(hand[1]))==1 and set(hand[0]) == set(range(min(hand[0]), min(hand[0])+5)),
             [max(hand[0])]),
          lambda hand: # Four of a kind - Return 4-card rank as high card.
             (any([hand[0].count(c)==4 for c in hand[0]]),
             [c for c in set(hand[0]) if hand[0].count(c)==4]),
          lambda hand: # Full house - Return 3-card rank then 2-card rank as high cards.
             (len(set(hand[0]))==2 and all([hand[0].count(c)==2 or hand[0].count(c)==3 for c in hand[0]]),
             [c for c in set(hand[0]) if hand[0].count(c)==3]+[c for c in set(hand[0]) if hand[0].count(c)==2]),
          lambda hand: # Flush - Return sorted cards as high cards
             (len(set(hand[1]))==1,
              sorted(hand[0], reverse=True)),
          lambda hand: # Straight - Return highest card in hand as high card
             (set(hand[0]) == set(range(min(hand[0]), min(hand[0])+5)),
             [max(hand[0])]),
          lambda hand: # Three of a kind - Return 3-card rank then ranks of other cards as high cards
             (any([hand[0].count(c)==3 for c in hand[0]]),
             [c for c in set(hand[0]) if hand[0].count(c)==3]+sorted([c for c in set(hand[0]) if hand[0].count(c)!=3], reverse=True)),
          lambda hand: # Two pair - Return 2-pair ranks and fifth card as high cards
             (len(set(hand[0]))==3 and sum([hand[0].count(c)==2 for c in hand[0]])==4,
              sorted([c for c in set(hand[0]) if hand[0].count(c)==2], reverse=True)+[c for c in set(hand[0]) if hand[0].count(c)!=2]),
          lambda hand: # One pair - Return pair rank then three others as high cards
             (len(set(hand[0]))==4 and sum([hand[0].count(c)==2 for c in hand[0]])==2,
             [c for c in set(hand[0]) if hand[0].count(c)==2]+sorted([c for c in set(hand[0]) if hand[0].count(c)!=2], reverse=True)),
          lambda hand: # High card
             (True, sorted(hand[0], reverse=True))]

# Parse file
f = open('poker.txt')
lines = f.readlines()
f.close()

player_one_wins = 0

for idx,line in enumerate(lines):
  line = line.strip().split(' ')

  # Parse out player hands
  player_one_cards = cards(line[:5])
  player_two_cards = cards(line[5:])
  
  # Return hand strength
  player_one_hand, player_one_highcards = ( (i,hand(player_one_cards)[1]) for i,hand in enumerate(hands) if hand(player_one_cards)[0]).next()
  player_two_hand, player_two_highcards = ( (i,hand(player_two_cards)[1]) for i,hand in enumerate(hands) if hand(player_two_cards)[0]).next()
 
  # Note that if there is a tie, we need to cycle through the high cards to see if player one beats player two. 
  if player_one_hand < player_two_hand:
    player_one_wins += 1
  elif player_one_hand == player_two_hand:
    player_one_wins += (1 if player_one_highcard > player_two_highcard else 0 for player_one_highcard,player_two_highcard in zip(player_one_highcards, player_two_highcards)
                       if player_one_highcard != player_two_highcard).next() 

print player_one_wins
