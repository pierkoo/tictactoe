# 27 Tic Tac Toe Bot

import random

def get_input(cor_h):
	valid=[1,2,3]
	while True:	
		while True:
			cor=input('Make a move (x,y) ')
			try:
				cor = [int(e) for e in cor.split(',')]
				break
			except ValueError:
				print('Wrong input, choose again')	
		if  len(cor) == 2:		
			if cor[0] in valid and cor[1] in valid:
				if cor not in cor_h:
					cor_h.append(cor)
					break
		print('Wrong move, choose again')

	return cor, cor_h

def bot_input(cor_h): # random moves - some logic to be implemented
	while True:	
	
		cor=[random.randrange(1,4),random.randrange(1,4)]

		if cor not in cor_h:
			cor_h.append(cor)
			break

	return cor, cor_h

def update_board(cor,player,board):
	if player == 1:
		mark='x'
	else:
		mark='o'

	board[cor[0]-1][cor[1]-1]=mark

	return board	

def print_g(game): #simplest posiible solution to print board-like table
	print('',game[0],'\n',game[1],'\n',game[2])		


def draw_board(board):
	size=range(len(board))
	top=''.join([' ___' for e in size])
	for i in size:
		print(top)
		side=''
		for j in size:
			elem=str(board[i][j])
			if elem=='0':
				elem=' '
			side=side+'| '+elem+' '
		side=side+'|'
		print(side)
	print(top)

def check_winner(board):
	game=board[:]

	for i in range(3):
		game.append([game[0][i],game[1][i],game[2][i]])
	
	game.append([game[0][2],game[1][1],game[2][0]])
	game.append([game[0][0],game[1][1],game[2][2]])

	if [e for e in game if 'x' in e and 0 not in e and 'o' not in e]:
		print('1 wins!')
		result=False
	elif [e for e in game if 'o' in e and 0 not in e and 'x' not in e]:
		print('2 wins!')
		result=False
	elif not [e for e in game if 0 in e]:
		print('Draw!')
		result=False
	else:
		print('No winner - game continues!')
		result=True
	return result		

def players():
	while True:
		players=int(input('How many players? '))
		if players == 2:
			break
		elif players == 1:
			print('You will play vs computer!')
			while True:
				start=(input('Do you want to start? y/n? '))
				if start=='y':
					print('You wil play as Player 1!')
					players=3
					break
				elif start=='n':
					players=4
					print('You wil play as Player 2!')
					break
				else:
					print('Incorrect input')
			break
		else:
			print('Please specify correct number of players: 1 or 2')
	return players 

def game(start):
	if start==2:
		print('Welcome in Tic Tac Toe for 2 players!')
	else:	
		print('Welcome in Tic Tac Toe for 1 player!')

	board = [[0,0,0],
	[0,0,0],
	[0,0,0]]
	counter=0 #this is implicit - to be straighten out
	cor_h=[]
	cont=True

	draw_board(board)
	
	while cont==True:
		player=counter%2+1

		print('Player',player)
		if start==2:
			cors=get_input(cor_h)
		else:
			if player==1:
				cors=bot_input(cor_h)
			else:	
				cors=get_input(cor_h)	
		cor=cors[0]
		cor_h=cors[1]
		board=update_board(cor,player,board)
		draw_board(board)
		cont=check_winner(board)
		counter+=1	

	

def tic_tac_toe():
	player=players()
	game(player)



tic_tac_toe()

#print(players())
