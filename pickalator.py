import random
import time

team1_name = 'RCB'
team2_name = 'CSK'

team1_rank = 1      # march madness has predetermined ranks through the regional qualifiers
team2_rank = 2

team1_chance = 16 - team1_rank # 16 teams in total so '16-'; lesser the rank higher the chance
team2_chance = 16 - team2_rank

team1_chance += random.randint(0,16)   # adding random values to add uncertainity
team2_chance += random.randint(0,16)

print('The pickalator is choosing a winner...\n')

time.sleep(2)  # real time calculation effect

print('....almost....\n')

time.sleep(2)

if team1_chance >= team2_chance:
    confidence = (team1_chance - team2_chance)/31 * 100 # calculating confidence/prediction confidence
    print(f'The Pickalator chose: {team1_name} with {int(confidence)}% confidence')
else:
    confidence = (team2_chance - team1_chance)/31 * 100
    print(f'The Pickalator chose: {team2_name} with {int(confidence)}% confidence')