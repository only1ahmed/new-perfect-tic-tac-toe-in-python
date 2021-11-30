def play(player,row):   
    # the matrix of the game display
    if player == 'one':
        s = 0
        sym = 'x'
    else:
        s = 1
        sym = 'o'

    # the display of the game table... we convert every single item to a string and put it in it's order acording to the game's original display...

    display = f"{row[0][0]}|{row[0][1]}|{row[0][2]}|{row[0][3]}|\n" \
                f"{row[1][0]}|{row[1][1]}|{row[1][2]}|{row[1][3]}|\n" \
                f"{row[2][0]}|{row[2][1]}|{row[2][2]}|{row[2][3]}|\n" \
                f"{row[3][0]}|{row[3][1]}|{row[3][2]}|{row[3][3]}|\n"
    print("player ",player,"'s turn (",sym,')')

    # i keep this part of the code looping till the player inputs a valid input... and when he does, i stop looping by setting "con" to "False"...
    con = True
    while con:
        # the player inputs the coordinates then i check the following:
        try:
            sel = input('input the coordinates: ' + '\n')
            #  1) if the player wanna exit the game...
            if sel == 'exit':
                exit()
            #  2) either the player did input the coordinates in the right form which is "xy" like "12" (without the quotations), by checking the length of the input..
            elif len(sel) == 2 and int(list(sel)[0]) > 0 and int(list(sel)[1]) > 0:

                # if he did so, we transform our string '(sel)' into a list so we can take every coordinate (x,y) separately
                # then we assign the values of the coordinates as integers
                
                # (we couldn't assign it as integers from the beginning as for example: if we have 12 as an input, the program will read it as 12 not as '1''2', so it will be harder to separate the coordinates but it's possible with some use of the modulo operator.) 
                    #(***) "we might try to assign a character instead of a number into an 'int' type..."
                sel,sel[0],sel[1] = list(sel),int(sel[0]),int(sel[1])

                # we check if the coordinate is already taken by another player previously
                if row[sel[0]][sel[1]] == 'x' or row[sel[0]][sel[1]] == 'o':
                    # if true we tell thr player to input another coords...
                    print('this square is full, select an empty square...' + '\n',display)
                else:
                    # if not we set 'x' in the coords
                    row[sel[0]][sel[1]] = sym
                    # and then we set "con" to "False" to stop the loop as he did input a valid coords...
                    con = False
                display = f"{row[0][0]}|{row[0][1]}|{row[0][2]}|{row[0][3]}|\n" \
                        f"{row[1][0]}|{row[1][1]}|{row[1][2]}|{row[1][3]}|\n" \
                        f"{row[2][0]}|{row[2][1]}|{row[2][2]}|{row[2][3]}|\n" \
                        f"{row[3][0]}|{row[3][1]}|{row[3][2]}|{row[3][3]}|\n"
                print('\n', display)

            # if he did input more than 2 coords "xy" like "123" for example.. we tell the player to input the right coords form.. then we start again as there is an active while loop...
            else:
                print('input the coordinates in the following form: "xy" as x,y are postive integers...' + '\n' + '\n',display)
            # i here assume that the player might have input a character instead of a number "ex: (ghdfghdfg)"... so, i made a ValueError check...
            # the error happens under the comment (***)
        except (IndexError,ValueError):
            print('reinput valid coordinates... \n',display)
            # i set the variable "sel" to a string again as it was assigned as a list up there, so we can loop again without a problem...
            sel = ''
            
 # welcome message       
print("""welcome to tic tac toe!
type the coordinates in this form : 'xy'
for example : 12 
the first coordinate represents the horizontal coordinate and the sekeepd represents the vertical one.
enjoy :)""")
keep = True
con = False
# a loop to keep the program running 
while keep:
    
  # the matrix of the game display
    s = 0
    row = [[' ','1','2','3'],
            ['1',' ',' ',' '],
            ['2',' ',' ',' '],
            ['3', ' ',' ',' ']]
    display = f"{row[0][0]}|{row[0][1]}|{row[0][2]}|{row[0][3]}|\n"\
            f"{row[1][0]}|{row[1][1]}|{row[1][2]}|{row[1][3]}|\n"\
            f"{row[2][0]}|{row[2][1]}|{row[2][2]}|{row[2][3]}|\n"\
            f"{row[3][0]}|{row[3][1]}|{row[3][2]}|{row[3][3]}|\n"
    print('\n', display)
    # checks whose turn
    for i in range(0,9):
        if i % 2 == 0:
            play('one',row)
        else:
            play('two',row)    
        display = f"{row[0][0]}|{row[0][1]}|{row[0][2]}|{row[0][3]}|\n"\
            f"{row[1][0]}|{row[1][1]}|{row[1][2]}|{row[1][3]}|\n"\
            f"{row[2][0]}|{row[2][1]}|{row[2][2]}|{row[2][3]}|\n"\
            f"{row[3][0]}|{row[3][1]}|{row[3][2]}|{row[3][3]}|\n"

   # time to check if any of the players won the game... the check iterates every loop of the 9 loops.. 
   # if a player won, the loop will be broke 
        #prints draw if the 9 loops ended without 
        # diagonal check
        if row[1][1] == row[2][2] and row[2][2] == row[3][3] and  'x' == row[2][2]:
            print('player one is the winner!')
            break
        elif row[1][1] == row[2][2] and row[2][2] == row[3][3] and  'o' == row[2][2]:
            print('player two is the winner!')
            break
        elif row[1][3] == row[2][2] and row[2][2] == row[3][1] and  'x' == row[2][2]:
            print('player one is the winner!')
            break
        elif row[1][3] == row[2][2] and row[2][2] == row[3][1] and  'o' == row[2][2]:
            print('player two is the winner!')            
            break
        # for the rows and columns check, we use the fact that the variable "con" is set false earlier... so we set it True so we can stop the outter loop..
        # rows check
        for i in range(1,4):
            if row[i][1] == row[i][2] and row[i][1] == row[i][3] and 'x' == row[i][1]:
                print('player one is the winner!')
                con = True
                break
            elif row[i][1] == row[i][2] and row[i][1] == row[i][3] and 'o' == row[i][1]:
                print('player two is the winner!')
                con = True
                break
        # this is how we stop the outter loop...
        if con:
            break
        # columns check
        for i in range(1,4):
            if row[1][i] == row[2][i] and row[1][i] == row[3][i] and 'x' == row[1][i]:
                print('player one is the winner!')
                con = True
                break
            elif row[1][i] == row[2][i] and row[1][i] == row[3][i] and 'o' == row[1][i]:
                print('player two is the winner!')
                con = True
                break
        if con:
            break
        elif display.count(" ") == 1:
            print('Draw!')
            break
    #after all of this we iterate all of that 9 times OR if a player wins, the loop will be broke...
    
    #now we check if the players wanna play again
    keep = input('do you want to play again ? (yes/no) \n')
    if keep.lower() == 'yes':
        keep = True
        con = False
    elif keep.lower() == 'no':
        keep = False
        print('\nthanks for playing the game \n') 
        bye = input('  press enter to exit')
    else:
        keep = False
        bye = input("i guess you don't want to play again...thanks for playing" + '\n' + 'press enter to exit')





   # this code is made by FCAI student: Ahmed Wesam...
   # special thanks for adham khaled for helping me improving it :) <3
   # remember me in your prayers :)