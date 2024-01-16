#Next step: use a dictionary to read out what the results of each round are 

import random, sys
wins = 0
losses = 0
ties = 0
#you should make this a function

rpskey = {'r':'rock', 'p':'paper', 's':'scissors'}
def print_score(wins, losses, ties): 
    print(f'Wins: {wins}, Losses: {losses}, Ties: {ties}')

choices = list(rpskey.keys())
while True: 
    
    
    while True: 
        print('Make your move (r)ock, (p)aper, (s)cissors')
        #need to take user input
        p1move = input(str()).lower() 
        p2move = random.choice(choices)
        if p1move not in choices:
            print('please enter a valid key: r, p, s or q')
        #add 1 to win 
            #if p1 rock & p2 scissors then p1 wins
            #if p1 paper & p2 rock then p1 wins 
            #if p1 scissors & p2 paper then p1 wins
        if (p1move == 'r' and p2move == 's') or (p1move == 'p' and p2move == 'r')  or (p1move == 's' and  p2move == 'p'): 
            wins += 1
            print(f'You won! You threw {rpskey.get(p1move)}, and the opponent threw {rpskey.get(p2move)}')
        
        #add 1 to loss
            #if p1 rock  & p2 paper then P2 wins
            #if p1 paper & p2 scissors then p2 wins
            #if p1 scissors & p2 rock then p2 wins
        elif (p1move == 'r' and p2move == 'p') or (p1move == 'p' and p2move == 's')  or (p1move == 's' and  p2move == 'r'):
            losses += 1 
            print(f'You lost =[. You threw {rpskey.get(p1move)}, and the opponent threw {rpskey.get(p2move)}')

        #add 1 to tie
            #if p1move == p2move then tie
        elif p1move == p2move:
            ties += 1
            print(f'Tie! You both threw {rpskey.get(p1move)}')
        
        elif p1move == 'q':
            print("Thanks for playing, bye.")
            sys.exit()
            
            
        print_score(wins,losses,ties)

    #conditionally handle the input
    #variable for random RPS p2






    #title menu
