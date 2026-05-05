# This program plays the Peg Game.
# It scores each game.
# It runs any number of games the user wants it to play at a time.
# It tells at the end how many games achieved particular scores.

import random

number_of_score_1s = 0
number_of_score_2s = 0
number_of_score_3s = 0
number_of_score_4s = 0
number_of_score_5s = 0
number_of_score_6s = 0
number_of_score_7s = 0
number_of_score_8s = 0
number_of_score_9s = 0
number_of_score_10s = 0

def print_matrix_to_file():
    line_1 = '\n' + '          ' + psn[0] + '                      ' + '0'
    line_2 = '\n' + '        ' + psn[1] + '   ' + psn[2] + '                  ' + '1' + '   ' + '2'
    line_3 = '\n' + '      ' + psn[3] + '   ' + psn[4] + '   ' + psn[5] + '              ' + '3' + '   ' + '4' + '   ' + '5'
    line_4 = '\n' + '    ' + psn[6] + '   ' + psn[7] + '   ' + psn[8] + '   ' + psn[9] + '          ' + '6' + '   ' + '7' + '   ' + '8' + '   ' + '9'
    line_5 = '\n' + '  ' + psn[10] + '   ' + psn[11] + '   ' + psn[12] + '   ' + psn[13] + '   ' + psn[14] + '     ' + '10' + '  ' + '11' + '  ' + '12' + '  ' + '13' + '  ' + '14'
    output_matrix = line_1 + line_2 + line_3 + line_4 + line_5
    f.write(output_matrix)

def list_possible_moves():
    # Case: 01 - Move 0 to 3, remove 1:
    if psn[0] == 'I' and psn[1] == 'I' and psn[3] == '-':
        possible_moves.append(1)
    # Case: 02 - Move 0 to 5, remove 2:
    if psn[0] == 'I' and psn[2] == 'I' and psn[5] == '-':
        possible_moves.append(2)
    # Case: 03 - Move 1 to 6, remove 3:
    if psn[1] == 'I' and psn[3] == 'I' and psn[6] == '-':
        possible_moves.append(3)
    # Case: 04 - Move 1 to 8, remove 4:
    if psn[1] == 'I' and psn[4] == 'I' and psn[8] == '-':
        possible_moves.append(4)
    # Case: 05 - Move 2 to 7, remove 4:
    if psn[2] == 'I' and psn[4] == 'I' and psn[7] == '-':
        possible_moves.append(5)
    # Case: 06 - Move 2 to 9, remove 5:
    if psn[2] == 'I' and psn[5] == 'I' and psn[9] == '-':
        possible_moves.append(6)
    # Case: 07 - Move 3 to 5, remove 4:
    if psn[3] == 'I' and psn[4] == 'I' and psn[5] == '-':
        possible_moves.append(7)
    # Case: 08 - Move 3 to 10, remove 6:
    if psn[3] == 'I' and psn[6] == 'I' and psn[10] == '-':
        possible_moves.append(8)
    # Case: 09 - Move 3 to 12, remove 7
    if psn[3] == 'I' and psn[7] == 'I' and psn[12] == '-':
        possible_moves.append(9)
    # Case: 10 - Move 4 to 11, remove 7:
    if psn[4] == 'I' and psn[7] == 'I' and psn[11] == '-':
        possible_moves.append(10)
    # Case: 11 - Move 4 to 13, remove 8:
    if psn[4] == 'I' and psn[8] == 'I' and psn[13] == '-':
        possible_moves.append(11)
    # Case: 12 - Move 5 to 12, remove 8:
    if psn[5] == 'I' and psn[8] == 'I' and psn[12] == '-':
        possible_moves.append(12)
    # Case: 13 - Move 5 to 14, remove 9:
    if psn[5] == 'I' and psn[9] == 'I' and psn[14] == '-':
        possible_moves.append(13)
    # Case: 14 - Move 6 to 8, remove 7:
    if psn[6] == 'I' and psn[7] == 'I' and psn[8] == '-':
        possible_moves.append(14)
    # Case: 15 - Move 7 to 9, remove 8:
    if psn[7] == 'I' and psn[8] == 'I' and psn[9] == '-':
        possible_moves.append(15)
    # Case: 16 - Move 10 to 12, remove 11:
    if psn[10] == 'I' and psn[11] == 'I' and psn[12] == '-':
        possible_moves.append(16)
    # Case: 17 - Move 11 to 13, remove 12:
    if psn[11] == 'I' and psn[12] == 'I' and psn[13] == '-':
        possible_moves.append(17)
    # Case: 18 - Move 12 to 14, remove 13:
    if psn[12] == 'I' and psn[13] == 'I' and psn[14] == '-':
        possible_moves.append(18)
    # Case: 19 - Move 3 to 0, remove 1:
    if psn[3] == 'I' and psn[1] == 'I' and psn[0] == '-':
        possible_moves.append(19)
    # Case: 20 - Move 5 to 0, remove 2:
    if psn[5] == 'I' and psn[2] == 'I' and psn[0] == '-':
        possible_moves.append(20)
    # Case: 21 - Move 6 to 1, remove 3:
    if psn[6] == 'I' and psn[3] == 'I' and psn[1] == '-':
        possible_moves.append(21)
    # Case: 22 - Move 8 to 1, remove 4:
    if psn[8] == 'I' and psn[4] == 'I' and psn[1] == '-':
        possible_moves.append(22)
    # Case: 23 - Move 7 to 2, remove 4:
    if psn[7] == 'I' and psn[4] == 'I' and psn[2] == '-':
        possible_moves.append(23)
    # Case: 24 - Move 9 to 2, remove 5:
    if psn[9] == 'I' and psn[5] == 'I' and psn[2] == '-':
        possible_moves.append(24)
    # Case: 25 - Move 5 to 3, remove 4:
    if psn[5] == 'I' and psn[4] == 'I' and psn[3] == '-':
        possible_moves.append(25)
    # Case: 26 - Move 10 to 3, remove 6:
    if psn[10] == 'I' and psn[6] == 'I' and psn[3] == '-':
        possible_moves.append(26)
    # Case: 27 - Move 12 to 3, remove 7:
    if psn[12] == 'I' and psn[7] == 'I' and psn[3] == '-':
        possible_moves.append(27)
    # Case: 28 - Move 11 to 4, remove 7:
    if psn[11] == 'I' and psn[7] == 'I' and psn[4] == '-':
        possible_moves.append(28)
    # Case: 29 - Move 13 to 4, remove 8:
    if psn[13] == 'I' and psn[8] == 'I' and psn[4] == '-':
        possible_moves.append(29)
    # Case: 30 - Move 12 to 5, remove 8:
    if psn[12] == 'I' and psn[8] == 'I' and psn[5] == '-':
        possible_moves.append(30)
    # Case: 31 - Move 14 to 5, remove 9:
    if psn[14] == 'I' and psn[9] == 'I' and psn[5] == '-':
        possible_moves.append(31)
    # Case: 32 - Move 8 to 6, remove 7:
    if psn[8] == 'I' and psn[7] == 'I' and psn[6] == '-':
        possible_moves.append(32)
    # Case: 33 - Move 9 to 7, remove 8:
    if psn[9] == 'I' and psn[8] == 'I' and psn[7] == '-':
        possible_moves.append(33)
    # Case: 34 - Move 12 to 10, remove 11:
    if psn[12] == 'I' and psn[11] == 'I' and psn[10] == '-':
        possible_moves.append(34)
    # Case: 35 - Move 13 to 11, remove 12:
    if psn[13] == 'I' and psn[12] == 'I' and psn[11] == '-':
        possible_moves.append(35)
    # Case: 36 - Move 14 to 12, remove 13:
    if psn[14] == 'I' and psn[13] == 'I' and psn[12] == '-':
        possible_moves.append(36)
    return possible_moves
    output_possible_moves_to_file = '\n\n Possible moves are ' + str(possible_moves)
    f.write(output_possible_moves_to_file)

def choose_move_number(m):
	# Case: 01 - Move 0 to 3, remove 1:
	#if psn[0] == 'I' and psn[1] == 'I' and psn[3] == '-':
	if m == 1:
		psn[0] = '-'
		psn[1] = '-'
		psn[3] = 'I'
		f.write('\n\n 0 to 3, remove 1')
		print_matrix_to_file()
		moves_made.append(1)
	# Case: 02 - Move 0 to 5, remove 2:
	#if psn[0] == 'I' and psn[2] == 'I' and psn[5] == '-':
	if m == 2:
		psn[0] = '-'
		psn[2] = '-'
		psn[5] = 'I'
		f.write('\n\n 0 to 5, remove 2')
		print_matrix_to_file()
		moves_made.append(2)
	# Case: 03 - Move 1 to 6, remove 3:
	#if psn[1] == 'I' and psn[3] == 'I' and psn[6] == '-':
	if m == 3:
		psn[1] = '-'
		psn[3] = '-'
		psn[6] = 'I'
		f.write('\n\n 1 to 6, remove 3')
		print_matrix_to_file()
		moves_made.append(3)
	# Case: 04 - Move 1 to 8, remove 4:
	#if psn[1] == 'I' and psn[4] == 'I' and psn[8] == '-':
	if m == 4:
		psn[1] = '-'
		psn[4] = '-'
		psn[8] = 'I'
		f.write('\n\n 1 to 8, remove 4')
		print_matrix_to_file()
		moves_made.append(4)
	# Case: 05 - Move 2 to 7, remove 4:
	#if psn[2] == 'I' and psn[4] == 'I' and psn[7] == '-':
	if m == 5:
		psn[2] = '-'
		psn[4] = '-'
		psn[7] = 'I'
		f.write('\n\n 2 to 7, remove 4')
		print_matrix_to_file()
		moves_made.append(5)
	# Case: 06 - Move 2 to 9, remove 5:
	#if psn[2] == 'I' and psn[5] == 'I' and psn[9] == '-':
	if m == 6:
		psn[2] = '-'
		psn[5] = '-'
		psn[9] = 'I'
		f.write('\n\n 2 to 9, remove 5')
		print_matrix_to_file()
		moves_made.append(6)
	# Case: 07 - Move 3 to 5, remove 4:
	#if psn[3] == 'I' and psn[4] == 'I' and psn[5] == '-':
	if m == 7:
		psn[3] = '-'
		psn[4] = '-'
		psn[5] = 'I'
		f.write('\n\n 3 to 5, remove 4')
		print_matrix_to_file()
		moves_made.append(7)
	# Case: 08 - Move 3 to 10, remove 6:
	#if psn[3] == 'I' and psn[6] == 'I' and psn[10] == '-':
	if m == 8:
		psn[3] = '-'
		psn[6] = '-'
		psn[10] = 'I'
		f.write('\n\n 3 to 10, remove 6')
		print_matrix_to_file()
		moves_made.append(8)
	# Case: 09 - Move 3 to 12, remove 7
	#if psn[3] == 'I' and psn[7] == 'I' and psn[12] == '-':
	if m == 9:
		psn[3] = '-'
		psn[7] = '-'
		psn[12] = 'I'
		f.write('\n\n 3 to 12, remove 7')
		print_matrix_to_file()
		moves_made.append(9)
	# Case: 10 - Move 4 to 11, remove 7:
	#if psn[4] == 'I' and psn[7] == 'I' and psn[11] == '-':
	if m == 10:
		psn[4] = '-'
		psn[7] = '-'
		psn[11] = 'I'
		f.write('\n\n 4 to 11, remove 7')
		print_matrix_to_file()
		moves_made.append(10)
	# Case: 11 - Move 4 to 13, remove 8:
	#if psn[4] == 'I' and psn[8] == 'I' and psn[13] == '-':
	if m == 11:
		psn[4] = '-'
		psn[8] = '-'
		psn[13] = 'I'
		f.write('\n\n 4 to 13, remove 8')
		print_matrix_to_file()
		moves_made.append(11)
	# Case: 12 - Move 5 to 12, remove 8:
	#if psn[5] == 'I' and psn[8] == 'I' and psn[12] == '-':
	if m == 12:
		psn[5] = '-'
		psn[8] = '-'
		psn[12] = 'I'
		f.write('\n\n 5 to 12, remove 8')
		print_matrix_to_file()
		moves_made.append(12)
	# Case: 13 - Move 5 to 14, remove 9:
	#if psn[5] == 'I' and psn[9] == 'I' and psn[14] == '-':
	if m == 13:
		psn[5] = '-'
		psn[9] = '-'
		psn[14] = 'I'
		f.write('\n\n 5 to 14, remove 9')
		print_matrix_to_file()
		moves_made.append(13)
	# Case: 14 - Move 6 to 8, remove 7:
	#if psn[6] == 'I' and psn[7] == 'I' and psn[8] == '-':
	if m == 14:
		psn[6] = '-'
		psn[7] = '-'
		psn[8] = 'I'
		f.write('\n\n 6 to 8, remove 7')
		print_matrix_to_file()
		moves_made.append(14)
	# Case: 15 - Move 7 to 9, remove 8:
	#if psn[7] == 'I' and psn[8] == 'I' and psn[9] == '-':
	if m == 15:
		psn[7] = '-'
		psn[8] = '-'
		psn[9] = 'I'
		f.write('\n\n 7 to 9, remove 8')
		print_matrix_to_file()
		moves_made.append(15)
	# Case: 16 - Move 10 to 12, remove 11:
	#if psn[10] == 'I' and psn[11] == 'I' and psn[12] == '-':
	if m == 16:
		psn[10] = '-'
		psn[11] = '-'
		psn[12] = 'I'
		f.write('\n\n 10 to 12, remove 11')
		print_matrix_to_file()
		moves_made.append(16)
	# Case: 17 - Move 11 to 13, remove 12:
	#if psn[11] == 'I' and psn[12] == 'I' and psn[13] == '-':
	if m == 17:
		psn[11] = '-'
		psn[12] = '-'
		psn[13] = 'I'
		f.write('\n\n 11 to 13, remove 12')
		print_matrix_to_file()
		moves_made.append(17)
	# Case: 18 - Move 12 to 14, remove 13:
	#if psn[12] == 'I' and psn[13] == 'I' and psn[14] == '-':
	if m == 18:
		psn[12] = '-'
		psn[13] = '-'
		psn[14] = 'I'
		f.write('\n\n 12 to 14, remove 13')
		print_matrix_to_file()
		moves_made.append(18)
	# Case: 19 - Move 3 to 0, remove 1:
	#if psn[3] == 'I' and psn[1] == 'I' and psn[0] == '-':
	if m == 19:
		psn[3] = '-'
		psn[1] = '-'
		psn[0] = 'I'
		f.write('\n\n 3 to 0, remove 1')
		print_matrix_to_file()
		moves_made.append(19)
	# Case: 20 - Move 5 to 0, remove 2:
	#if psn[5] == 'I' and psn[2] == 'I' and psn[0] == '-':
	if m == 20:
		psn[5] = '-'
		psn[2] = '-'
		psn[0] = 'I'
		f.write('\n\n 5 to 0, remove 2')
		print_matrix_to_file()
		moves_made.append(20)
	# Case: 21 - Move 6 to 1, remove 3:
	#if psn[6] == 'I' and psn[3] == 'I' and psn[1] == '-':
	if m == 21:
		psn[6] = '-'
		psn[3] = '-'
		psn[1] = 'I'
		f.write('\n\n 6 to 1, remove 3')
		print_matrix_to_file()
		moves_made.append(21)
	# Case: 22 - Move 8 to 1, remove 4:
	#if psn[8] == 'I' and psn[4] == 'I' and psn[1] == '-':
	if m == 22:
		psn[8] = '-'
		psn[4] = '-'
		psn[1] = 'I'
		f.write('\n\n 8 to 1, remove 4')
		print_matrix_to_file()
		moves_made.append(22)
	# Case: 23 - Move 7 to 2, remove 4:
	#if psn[7] == 'I' and psn[4] == 'I' and psn[2] == '-':
	if m == 23:
		psn[7] = '-'
		psn[4] = '-'
		psn[2] = 'I'
		f.write('\n\n 7 to 2, remove 4')
		print_matrix_to_file()
		moves_made.append(23)
	# Case: 24 - Move 9 to 2, remove 5:
	#if psn[9] == 'I' and psn[5] == 'I' and psn[2] == '-':
	if m == 24:
		psn[9] = '-'
		psn[5] = '-'
		psn[2] = 'I'
		f.write('\n\n 9 to 2, remove 5')
		print_matrix_to_file()
		moves_made.append(24)
	# Case: 25 - Move 5 to 3, remove 4:
	#if psn[5] == 'I' and psn[4] == 'I' and psn[3] == '-':
	if m == 25:
		psn[4] = '-'
		psn[5] = '-'
		psn[3] = 'I'
		f.write('\n\n 5 to 3, remove 4')
		print_matrix_to_file()
		moves_made.append(25)
	# Case: 26 - Move 10 to 3, remove 6:
	#if psn[10] == 'I' and psn[6] == 'I' and psn[3] == '-':
	if m == 26:
		psn[10] = '-'
		psn[6] = '-'
		psn[3] = 'I'
		f.write('\n\n 10 to 3, remove 6')
		print_matrix_to_file()
		moves_made.append(26)
	# Case: 27 - Move 12 to 3, remove 7:
	#if psn[12] == 'I' and psn[7] == 'I' and psn[3] == '-':
	if m == 27:
		psn[12] = '-'
		psn[7] = '-'
		psn[3] = 'I'
		f.write('\n\n 12 to 3, remove 7')
		print_matrix_to_file()
		moves_made.append(27)
	# Case: 28 - Move 11 to 4, remove 7:
	#if psn[11] == 'I' and psn[7] == 'I' and psn[4] == '-':
	if m == 28:
		psn[11] = '-'
		psn[7] = '-'
		psn[4] = 'I'
		f.write('\n\n 11 to 4, remove 7')
		print_matrix_to_file()
		moves_made.append(28)
	# Case: 29 - Move 13 to 4, remove 8:
	#if psn[13] == 'I' and psn[8] == 'I' and psn[4] == '-':
	if m == 29:
		psn[13] = '-'
		psn[8] = '-'
		psn[4] = 'I'
		f.write('\n\n 13 to 4, remove 8')
		print_matrix_to_file()
		moves_made.append(29)
	# Case: 30 - Move 12 to 5, remove 8:
	#if psn[12] == 'I' and psn[8] == 'I' and psn[5] == '-':
	if m == 30:
		psn[12] = '-'
		psn[8] = '-'
		psn[5] = 'I'
		f.write('\n\n 12 to 5, remove 8')
		print_matrix_to_file()
		moves_made.append(30)
	# Case: 31 - Move 14 to 5, remove 9:
	#if psn[14] == 'I' and psn[9] == 'I' and psn[5] == '-':
	if m == 31:
		psn[14] = '-'
		psn[9] = '-'
		psn[5] = 'I'
		f.write('\n\n 14 to 5, remove 9')
		print_matrix_to_file()
		moves_made.append(31)
	# Case: 32 - Move 8 to 6, remove 7:
	#if psn[8] == 'I' and psn[7] == 'I' and psn[6] == '-':
	if m == 32:
		psn[8] = '-'
		psn[7] = '-'
		psn[6] = 'I'
		f.write('\n\n 8 to 6, remove 7')
		print_matrix_to_file()
		moves_made.append(32)
	# Case: 33 - Move 9 to 7, remove 8:
	#if psn[9] == 'I' and psn[8] == 'I' and psn[7] == '-':
	if m == 33:
		psn[9] = '-'
		psn[8] = '-'
		psn[7] = 'I'
		f.write('\n\n 9 to 7, remove 8')
		print_matrix_to_file()
		moves_made.append(33)
	# Case: 34 - Move 12 to 10, remove 11:
	#if psn[12] == 'I' and psn[11] == 'I' and psn[10] == '-':
	if m == 34:
		psn[12] = '-'
		psn[11] = '-'
		psn[10] = 'I'
		f.write('\n\n 12 to 10, remove 11')
		print_matrix_to_file()
		moves_made.append(34)
	# Case: 35 - Move 13 to 11, remove 12:
	#if psn[13] == 'I' and psn[12] == 'I' and psn[11] == '-':
	if m == 35:
		psn[13] = '-'
		psn[12] = '-'
		psn[11] = 'I'
		f.write('\n\n 13 to 11, remove 12')
		print_matrix_to_file()
		moves_made.append(35)
	# Case: 36 - Move 14 to 12, remove 13:
	#if psn[14] == 'I' and psn[13] == 'I' and psn[12] == '-':
	if m == 36:
		psn[14] = '-'
		psn[13] = '-'
		psn[12] = 'I'
		f.write('\n\n 14 to 12, remove 13')
		print_matrix_to_file()
		moves_made.append(36)

def get_the_score():
    counter = 0
    if psn[0] == 'I': counter += 1
    if psn[1] == 'I': counter += 1
    if psn[2] == 'I': counter += 1
    if psn[3] == 'I': counter += 1
    if psn[4] == 'I': counter += 1
    if psn[5] == 'I': counter += 1
    if psn[6] == 'I': counter += 1
    if psn[7] == 'I': counter += 1
    if psn[8] == 'I': counter += 1
    if psn[9] == 'I': counter += 1
    if psn[10] == 'I': counter += 1
    if psn[11] == 'I': counter += 1
    if psn[12] == 'I': counter += 1
    if psn[13] == 'I': counter += 1
    if psn[14] == 'I': counter += 1
    return counter

number_of_games = int(input('How many games do you want to play? '))
f = open('Solver_Peg_Game_output.txt','w')

for n in range(0,number_of_games):
    # The setup:
    psn = ['I','I','I','I','-','I','I','I','I','I','I','I','I','I','I']
    moves_made = []
    possible_moves = []

    f.write('\n\n Initial matrix: \n')
    print_matrix_to_file()

    move_possible = True
    while move_possible == True:
        L = list_possible_moves()
        if len(L) >= 1:
            choose_move_number(random.choice(L))
        elif len(L) == 0:
            move_possible = False
        del L[:]

    list_of_moves_made_in_game = '\n\n Moves made: ' + str(moves_made)
    f.write(list_of_moves_made_in_game)
    score = get_the_score()
    score_report = '\n\n Score: ' + str(score)
    f.write(score_report)

    if score == 1: number_of_score_1s += 1
    if score == 2: number_of_score_2s += 1
    if score == 3: number_of_score_3s += 1
    if score == 4: number_of_score_4s += 1
    if score == 5: number_of_score_5s += 1
    if score == 6: number_of_score_6s += 1
    if score == 7: number_of_score_7s += 1
    if score == 8: number_of_score_8s += 1
    if score == 9: number_of_score_9s += 1
    if score == 10: number_of_score_10s += 1

line_n_of_summary = '\n\nIn ' + str(number_of_score_1s) + ' out of ' + str(number_of_games) + ' games, the program scored 1.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_2s) + ' out of ' + str(number_of_games) + ' games, the program scored 2.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_3s) + ' out of ' + str(number_of_games) + ' games, the program scored 3.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_4s) + ' out of ' + str(number_of_games) + ' games, the program scored 4.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_5s) + ' out of ' + str(number_of_games) + ' games, the program scored 5.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_6s) + ' out of ' + str(number_of_games) + ' games, the program scored 6.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_7s) + ' out of ' + str(number_of_games) + ' games, the program scored 7.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_8s) + ' out of ' + str(number_of_games) + ' games, the program scored 8.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_9s) + ' out of ' + str(number_of_games) + ' games, the program scored 9.'
f.write(line_n_of_summary)
line_n_of_summary = '\nIn ' + str(number_of_score_10s) + ' out of ' + str(number_of_games) + ' games, the program scored 10.'
f.write(line_n_of_summary)

f.close()
