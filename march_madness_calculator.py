#!/usr/bin/python
import random
import csv
import sys

'''
This script takes 538 probabilities for March Madness and *simulates* a tournament
using those probabilities. Note: to be as variant as March Madness usually is,
the script runs each possiblity one time (rather than standard practice simulating
multiple runs and taking the average.)

'''

def print_winner(winner, loser, chances, prob, symb):
    print(winner['team_name'] + ' wins over ' + loser['team_name'] + '\t\t\t' + str(chances) + ' ' + symb + ' ' + str(prob))
    return

def pick_winners(team1, team2, rnd=2):
    rd = 'rd' + str(rnd) + '_win'
    prev_rd = 'rd' + str(rnd - 1) + '_win'

    team1_bayesian_prob = team1[rd] / team1[prev_rd]
    team2_bayesian_prob = team2[rd] / team2[prev_rd]

    team1_over_team2_prob = team1_bayesian_prob / (team1_bayesian_prob + team2_bayesian_prob)

    chances = random.random()

    if chances <= team1_over_team2_prob:
        print_winner(team1, team2, chances, team1_over_team2_prob, '<')
        return team1
    elif chances > team1_over_team2_prob:
        print_winner(team2, team1, chances, team1_over_team2_prob, '>')
        return team2
    else: #never gets here
        print_winner(team1, team2, chances, team1_over_team2_prob, '<')
        return team1

def calculate_conf_winners(arr, rnd = 2):
    winners = []
    print ('Round ' + str(rnd) + ':')
    while (len(arr) != 0):
        if len(arr) % 2 != 0:
            print ('array is not even length')
            return
        if len(arr) == 2:
            pick_winners(arr[0], arr[1], rnd)
            return
        indexes_to_remove = []
        newarr = []

        #top and bottom
        indexes_to_remove.append(0)
        indexes_to_remove.append(len(arr) - 1)
        top_and_bottom_winner = pick_winners(arr[0], arr[len(arr) - 1], rnd)

        #mids
        indexes_to_remove.append(len(arr) // 2 - 1)
        indexes_to_remove.append(len(arr) // 2)
        mids_winner = pick_winners(arr[len(arr) // 2 - 1], arr[len(arr) // 2], rnd)

        winners = winners[:len(winners) // 2] + [top_and_bottom_winner] + [mids_winner] + winners[len(winners) // 2:]

        for i, x in enumerate(arr):
            if i in indexes_to_remove:
                pass
            else:
                newarr.append(arr[i])

        if len(newarr) == 0:
            arr = winners
            winners = []
            rnd += 1
            print ('Round ' + str(rnd) + ':')
        else:
            arr = newarr

def open_and_parse_file(filename='fivethirtyeight_ncaa_forecasts_2019.csv'):
    conference_and_teams = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['team_region'] not in conference_and_teams:
                conference_and_teams[row['team_region']] = []

            conference_and_teams[row['team_region']].append(
                {
                    'gender': row['gender'],
                    'team_name': row['team_name'],
                    'seed': int(row['team_seed']),
                    'conference': row['team_region'],
                    'rd1_win': float(row['rd1_win']),
                    'rd2_win': float(row['rd2_win']),
                    'rd3_win': float(row['rd3_win']),
                    'rd4_win': float(row['rd4_win']),
                    'rd5_win': float(row['rd5_win'])                
                }
            )
    for obj in conference_and_teams:
        arr = conference_and_teams[obj]
        conference_and_teams[obj] = sorted(arr, key=lambda x: x['seed'])
    for obj in conference_and_teams:
        print(conference_and_teams[obj][0]['gender'] + ' ' + conference_and_teams[obj][0]['conference'])
        print('---------------')
        print()
        calculate_conf_winners(conference_and_teams[obj])
        print()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ('Opening and generating possibilities with selected file...')
        open_and_parse_file(sys.argv[1])
    else:
        print ('Opening and generating possibilities with default file...')
        open_and_parse_file()
