ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards = lambda hand: zip(*[[ranks.index(card[0:-1]), card[-1]] for card in hand])
hands = [ lambda hand: # Royal Flush 
             len(set(hand[1]))==1 and set(hand[0]) == set(range(ranks.index('T'), ranks.index('T')+5)), \
          lambda hand: # Straight Flush
             len(set(hand[1]))==1 and set(hand[0]) == set(range(min(hand[0]), min(hand[0])+5)),
          lambda hand: # Four of a kind
             any([hand[0].count(c)==4 for c in hand[0]]),
          lambda hand: # Full house
             len(set(hand[0]))==2 and all([hand[0].count(c)==2 or hand[0].count(c)==3 for c in hand[0]]),
          lambda hand: # Flush
             len(set(hand[1]))==1,
          lambda hand: # Straight
             set(hand[0]) == set(range(min(hand[0]), min(hand[0])+5)),
          lambda hand: # Three of a kind
             any([hand[0].count(c)==3 for c in hand[0]]),
          lambda hand: # Two pair
             len(set(hand[0]))==3 and sum([hand[0].count(c)==2 for c in hand[0]])==4,
          lambda hand: # One pair
             len(set(hand[0]))==4 and sum([hand[0].count(c)==2 for c in hand[0]])==2,
          lambda hand: # High card
             True]

hand_names = ['Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight',
              'Three of a Kind', 'Two Pair', 'One Pair', 'High Card']

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
  player_one_hand = (i for i,hand in enumerate(hands) if hand(player_one_cards)).next()
  player_two_hand = (i for i,hand in enumerate(hands) if hand(player_two_cards)).next()
  
  if player_one_hand < player_two_hand:
    print 'Hand %i: Player One wins (%s vs %s)'%(idx, hand_names[player_one_hand], hand_names[player_two_hand])
    player_one_wins += 1
  elif player_one_hand == player_two_hand:
    player_one_hand_set = set(player_one_cards[0]).difference(player_two_cards[0])
    player_two_hand_set = set(player_two_cards[0]).difference(player_one_cards[0])
    if max(player_one_hand_set) > max(player_two_hand_set):
      print 'Hand %i: Player One wins (%s vs %s)'%(idx, hand_names[player_one_hand], hand_names[player_two_hand])
      player_one_wins += 1
  else:
    print 'Hand %i: Player Two wins (%s vs %s)'%(idx, hand_names[player_one_hand], hand_names[player_two_hand])

print player_one_wins
