---
layout: post
title: "Enova Hackathon"
date: 2013-10-25 13:25:00
categories: code
custom_css:
- syntax
---
Yesterday Enova hosted a hackathon on the Purdue campus, but not in the traditional sense. Instead of everyone making a unique project that would then be subjectively judged, the people at Enova built an online poker game. The task at hand was to build a bot that would contact the server to determine the game state, then if it was the bot's turn to play, make a move. It was a pretty standard poker game. You started with $1000 with a small blind of $10 and a big blind of $20. Throughout the game as players were eliminated the blinds increased and the game started to move faster.

For the first few practice rounds, our bot (TJ Root and myself) stayed ahead of the crowd. We were one of the first teams to have a stable handling of POST and GET requests as well as the basic JSON parsing. We placed in the top five in the first round, and again in the second, although I do not remember the exact placement. For the final practice round we hit a sweet spot with our bot, and it flew ahead with a very clear and decisive victory. After that, we decided not to change our code, and wished to play it safe for the actual tournament. Unfortunately there were some people that gave up working on thinking bots and randomly bet. Our bot's tendency to play a hand when it had already committed to a blind was no longer safe, as the other players at the table were no longer logical. We got hit hard quickly and had to pull that logic. With a bot that played it safer, we slowly crept up again. From a near defeat we pulled back up into fourth place. First and Fourth had bots that followed poker logic and worked to play a smart game, while second and third got lucky with random number generators. Unfortunately fourth didn't walk home with a prize, but it was still a blast.

The code is below. We adjusted the number of pairs needed to keep betting and the way the bot handled blinds depending on the way other players were responding.

```python
import requests
import time
import json
urlPart = 'http://nolimitcodeem.com/api/players/'
#key = 'deal-phase-key'
name = 'I think I can!'
#key = '49ca8489-bff3-4c69-8c9d-417e5c5f6d07'
#key = 'turn-phase-key'
#key = 'river-phase-key'
#key = 'e3e9f744-fa73-42a7-9583-706058a8993c' #Actual KEY
key = '47aa756c-db57-4ed8-9e01-090bf43606f1'
url = urlPart + key

# GET
def game_state():
  r = requests.get(url)
  return r.json()

# POST
def player_action(action):
  r = requests.post(url + action)
  return r.json()

def pair_exists(card1,card2):
  if (card1[0] == card2[0]):
    return 1
  return 0

def suit_match(card1,card2):
  if (card1[1] == card2[1]):
    return 1
  return 0

def card_match(card1,card2,search1,search2):
  if (card1[0] == search1 and card2[0] == search2):
    return 1
  elif (card2[0] == search1 and card1[0] == search2):
    return 1
  else:
    return 0

def not_deal(cards):
  #build hash
  dic = {}
  for card in cards:
    if (card[0] in dic):
      dic[card[0]] = dic[card[0]] + 1
    else:
      dic[card[0]] = 1

  #Check for 3 of a kind or more
  pairCount = 0
  for item in dic.values():
    if (item >= 3):
      return 'call'
    if (item >= 2):
      pairCount = pairCount + 1

  if (pairCount >= 1):
    return 'call'

  for item in dic:
    if (dic[item] >= 2):
      if (item == 'A' or item == 'K' or item == 'Q' or item == 'J'):
        return 'call'
  return 'fold'

def poker():
  run = 1
  while (run):
    time.sleep(1)

    turn_data = game_state()

    if (turn_data["your_turn"]):

      playerNum = len(turn_data["players_at_table"])
      myNum = 0
      count = 0
      for i in turn_data["players_at_table"]:
        if (i['player_name'] == name):
          myNum = count
        count = count + 1
      action = '/action?action_name='
      cards = turn_data["community_cards"] + turn_data["hand"]
      pos = float(myNum)/float(playerNum)
      print "-------------------------------------------"
      print "-------------------------------------------"
      print "-------------------------------------------"
      print "-------------------------------------------"
      if (turn_data['call_amount'] == 0):
        action = action + "check"
      else:
        if  (turn_data["betting_phase"] == "deal"):

          print "deal phase"
          #if (turn_data["current_bet"] != 0):
          #  action = action + "call"
          #if (turn_data["current_bet"] <= 20 and turn_data["current_bet"] > 0):
          #  action = action + "call"
          #  print "Auto Call"
          if (cards[0][0] == 'A' or cards[1][0] == 'A' or cards[0][0] == 'K' or cards[1][0] == 'K'):
            action = action + "call"
            print "Has an Ace"
          elif (pair_exists(cards[0],cards[1])):
            action = action + 'call'
            #if (cards[0][0] == 'A' or cards[0][0] == 'K' or cards[0][0] == 'Q' or cards[0][0] == 'J' or cards[0][0] == 'T' or cards[0][0] == '9' or cards[0][0] == '8'):
            #  action = action + "call"
            #  print "High Pair"
            #else:
            #  action = action + "fold"
            #  print "Bad Pair"
          elif (suit_match(cards[0],cards[1])):
            if (card_match(cards[0],cards[1],'A','K') or card_match(cards[0],cards[1],'A','Q') or card_match(cards[0],cards[1],'Q','K') or card_match(cards[0],cards[1],'A','T') or card_match(cards[0],cards[1],'Q','J') or card_match(cards[0],cards[1],'T','K') or card_match(cards[0],cards[1],'Q','T') or card_match(cards[0],cards[1],'J','T')):
              action = action + "call"
              print "Good Start"
            else:
              action = action + "fold"

          else:
            action = action + "fold"
        elif (turn_data["betting_phase"] == "flop"):
          if (turn_data['hand'][0][0] == 'A' or turn_data['hand'][1][0] == 'A' or turn_data['hand'][0][0] == 'K' or turn_data['hand'][1][0] == 'K'):
            action = action + 'call'
          else:
            action = action + not_deal(cards)
        #  action = action + "call"
        #elif (turn_data["betting_phase"] == "turn"):
        #  action = action + "call"
        #elif (turn_data["betting_phase"] == "river"):
        #  action = action + "call"
        else:
          action = action + not_deal(cards)

      print ""
      print cards
      print action[20:]
      print "Before Turn: " + str(turn_data['initial_stack'])
      print "In Hand: " + str(turn_data['stack'])
      print "Current Bet: " + str(turn_data['current_bet'])
      response = player_action(action)
      run = 1
poker()
```
