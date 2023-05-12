def move(board):
    values={}
    for i in range(3):
        for j in range(3):
            values[str(i)+str(j)]=board[i][j]
    us=[]
    them=[]
    empty=[]
    empty_corners=[]
    empty_edges=[]
    empty_middle=[]
    for key in values:
        if values[key]=="U":
            us.append(key)
        elif values[key]=="T":
            them.append(key)
        else:
            empty.append(key)
            if key=="00" or key=="02" or key=="20" or key=="22":
                empty_corners.append(key)
            elif key=="01" or key=="10" or key=="21" or key=="12":
                empty_edges.append(key)
            else:
                empty_middle.append(key)
    for char in "UT":
        for i in range(3):
            if values[str(i)+"0"]==char and values[str(i)+"1"]==char and values[str(i)+"2"]==" ":
                return (i,2)
        for i in range(3):
            if values[str(i)+"0"]==char and values[str(i)+"2"]==char and values[str(i)+"1"]==" ":
                return (i,1)
        for i in range(3):
            if values[str(i)+"1"]==char and values[str(i)+"2"]==char and values[str(i)+"0"]==" ":
                return (i,0)
        for j in range(3):
            if values["0"+str(j)]==char and values["1"+str(j)]==char and values["2"+str(j)]==" ":
                return (2,j)
        for j in range(3):
            if values["0"+str(j)]==char and values["2"+str(j)]==char and values["1"+str(j)]==" ":
                return (1,j)
        for j in range(3):
            if values["1"+str(j)]==char and values["2"+str(j)]==char and values["0"+str(j)]==" ":
                return (0,j)
        if values["00"]==char and values["11"]==char and values["22"]==" ":
            return (2,2)
        if values["00"]==char and values["22"]==char and values["11"]==" ":
            return (1,1)
        if values["11"]==char and values["22"]==char and values["00"]==" ":
            return (0,0)
        if values["02"]==char and values["11"]==char and values["20"]==" ":
            return (2,0)
        if values["02"]==char and values["20"]==char and values["11"]==" ":
            return (1,1)
        if values["11"]==char and values["20"]==char and values["02"]==" ":
            return (0,2)
    for char in "U":
        if values["00"]==char and values["22"]==char and values["02"]==" " and values["01"]==" " and values["12"]==" ":
            return (0,2)
        if values["00"]==char and values["22"]==char and values["20"]==" " and values["10"]==" " and values["21"]==" ":
            return (0,2)
        if values["20"]==char and values["02"]==char and values["00"]==" " and values["01"]==" " and values["10"]==" ":
            return (0,0)
        if values["20"]==char and values["02"]==char and values["22"]==" " and values["21"]==" " and values["12"]==" ":
            return (0,2)
    for char in "T":
        if values["00"]==char and values["22"]==char and values["02"]==" " and values["01"]==" " and values["12"]==" ":
            return (0,1)
        if values["00"]==char and values["22"]==char and values["20"]==" " and values["10"]==" " and values["21"]==" ":
            return (1,0)
        if values["20"]==char and values["02"]==char and values["00"]==" " and values["01"]==" " and values["10"]==" ":
            return (0,1)
        if values["20"]==char and values["02"]==char and values["22"]==" " and values["21"]==" " and values["12"]==" ":
            return (2,1)
    if len(empty)==9:
        return (2,0)
    if len(empty)==8 and values["11"]==" ":
        return (1,1)
    if len(empty)==8:
        return (2,0)
    if len(empty)==7 and values["02"]==" ":
        return (0,2)
    if len(empty)==7:
        return (1,1)
    if board==[[" "," "," "],[" ","U","T"],[" ","T"," "]]:
        return (2,2)
    if len(empty)==6 and len(empty_edges)==2:
        return (int(empty_corners[0][0]),int(empty_corners[0][1]))
    if board==[["T"," "," "],[" ","U"," "],[" ","T"," "]]:
        return (2,0)
    if board==[[" "," ","T"],[" ","U"," "],[" ","T"," "]]:
        return (2,2)
    if board==[["T"," "," "],[" ","U","T"],[" "," "," "]]:
        return (0,2)
    if board==[[" "," "," "],[" ","U","T"],["T"," "," "]]:
        return (2,2)
    if board==[[" ","T"," "],[" ","U"," "],["T"," "," "]]:
        return (0,0)
    if board==[[" ","T"," "],[" ","U"," "],[" "," ","T"]]:
        return (0,2)
    if board==[[" "," ","T"],["T","U"," "],[" "," "," "]]:
        return (0,0)
    if board==[[" "," "," "],["T","U"," "],[" "," ","T"]]:
        return (2,0)
    if board==[[" "," ","T"],["T","U"," "],["U"," "," "]]:
        return (2,2)
    if board==[[" "," ","T"],[" ","U"," "],["U","T"," "]]:
        return (0,0)
    if len(empty)==6 and not (values["11"]=="U" and values["12"]=="T"):
        return (int(empty_corners[0][0]),int(empty_corners[0][1]))
    if len(empty)==6:
        return (int(empty_edges[0][0]),int(empty_edges[0][1]))
    return (int(empty[0][0]),int(empty[0][1]))
def game_result(board):
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        if not board[0][0] == " ":
            return True, board[0][0]
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        if not board[1][0] == " ":
            return True, board[1][0]
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        if not board[2][0] == " ":
            return True, board[2][0]
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        if not board[0][0] == " ":
            return True, board[0][0]
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        if not board[0][1] == " ":
            return True, board[0][1]
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        if not board[0][2] == " ":
            return True, board[0][2]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if not board[0][0] == " ":
            return True, board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if not board[0][2] == " ":
            return True, board[0][2]
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False, "Continue"
    return True, "Draw"
def pivot_board(board, player):
    pivoted_board = [["?","?","?"],["?","?","?"],["?","?","?"]]
    if player == "X":
        replacement_dictionary = {" ": " ", "X": "U", "O": "T"}
    else:
        replacement_dictionary = {" ": " ", "X": "T", "O": "U"}
    for i in range(3):
        for j in range(3):
            pivoted_board[i][j] = replacement_dictionary[board[i][j]]
    return pivoted_board
def print_board(board):
    print("{0}|{1}|{2}\n-----\n{3}|{4}|{5}\n-----\n{6}|{7}|{8}\n".format(board[0][0], board[0][1], board[0][2],
                                                                     board[1][0], board[1][1], board[1][2],
                                                                     board[2][0], board[2][1], board[2][2]))
def test_game():
    game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    current_player = "X"
    game_done = False
    while not game_done:
        #print(current_player + "'s turn...")
        #Gets next move based on the current board, pivoting it
        #to show the player's own moves as U and the opponent's
        #as T.
        if current_player=="X":
            result = move(pivot_board(game_board, current_player))
        else:
            result = (int(input("What row? "))-1,int(input("What column? "))-1)
        #Checks if result is a tuple with two items, and prints
        #INVALID MOVE if not. Quits the game if the move is not
        #valid.
        try:
            row, column = result
        except:
            print("INVALID MOVE:", result)
            break
        #Checks if the move is legal, e.g. consists of two integers
        #in range and is not a move on top of an existing move.
        #Prints INVALID MOVE if not. Quits the game if the move
        #is not valid.
        try:
            if not game_board[row][column] == " ":
                print("INVALID MOVE:", row, column)
                break
            #Updates the game board if the move appeared valid.
            game_board[row][column] = current_player
        except:
            print("INVALID MOVE:", row, column)
            break
        #Changes the current player.
        current_player = "O" if current_player == "X" else "X"
        #Prints the current board.
        print_board(game_board)
        #Checks if the game has a winner or is a draw.
        game_done, winner = game_result(game_board)
    #Prints the final result if the game finished completely
    #(no invalid moves).
    if game_done:
        if winner == "Draw":
            print("It's a draw!")
        else:
            print(winner, "wins!")
for i in range(0,1000):
    test_game()
