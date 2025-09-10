'''
Task:
Read picture of chessboard position and print in chess notation

Input:
Consists of an ASCII-art picture of a chessboard with chess 
pieces on positions described by the input. The pieces of 
the white player are shown in upper-case, while the black
player's pieces are lower-case.

White - UPPER CASE
Black - lower case

K - King
Q - Queen
R - Rook
B - Bishop
N - Knight
P - Pawn

Chessboard outlines: + - |
Black fields are filled with :
White fields are filled with .

-----------------------------------------------------------

Output:
Consists of two lines. The forst line consists of the string
"White: ", followed by the description of positions of the 
pieces of the white player.

The second line consists of the string "Black: ", followed by
the description of the black player.

The description of the positions of the pieces is a 
comma-separeted list of terms (without spaces) describing the
pieces of the appropriate player. The description of a piece
consists of a single upper-case letter that denotes the type 
of the piece (except for pawns, for that this identifier is 
omitted). This letter is immediatelly followed by the position 
of the piece in the standard chess notation - a lower-case 
letter between “a” and “h” that determines the column (“a” is 
the leftmost column in the input) and a single digit between 1 
and 8 that determines the row (8 is the first row in the input).

The pieces in the description must appear in the following order:
Kings
Queens
Rooks
Bishops
Knights
Pawns

Note that the numbers of pieces may differ from the initial 
position, and might not even correspond to a situation that 
could arise in a valid chess game.

In case two piees of the same type appear in the input, the piece
with the smaller row number must be described before the other 
one if the pieces are white, and the one with the larger number
must be descrived first if the pieces are black. If two pieces of
the same type appear in the same row, the one with the smaller 
column letter must appear first.

-----------------------------------------------------------

Sample Input 1:
+---+---+---+---+---+---+---+---+
|.r.|:::|.b.|:q:|.k.|:::|.n.|:r:|
+---+---+---+---+---+---+---+---+
|:p:|.p.|:p:|.p.|:p:|.p.|:::|.p.|
+---+---+---+---+---+---+---+---+
|...|:::|.n.|:::|...|:::|...|:p:|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|.P.|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:P:|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|.P.|:::|.P.|:P:|...|:P:|.P.|:P:|
+---+---+---+---+---+---+---+---+
|:R:|.N.|:B:|.Q.|:K:|.B.|:::|.R.|
+---+---+---+---+---+---+---+---+

Samlpe Output 1:
White: Ke1,Qd1,Ra1,Rh1,Bc1,Bf1,Nb1,a2,c2,d2,f2,g2,h2,a3,e4
Black: Ke8,Qd8,Ra8,Rh8,Bc8,Ng8,Nc6,a7,b7,c7,d7,e7,f7,h7,h6

Sample Input 2:
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|.k.|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:k:|...|:::|...|
+---+---+---+---+---+---+---+---+

Sample Output 2:
White: 
Black: Kh5,Ke1
'''

#input is 17 lines in total

board = []
white = []
black = []
column = ["a","b","c","d","e","f","g","h"]

white_out = []
black_out = []

for i in range(17):
    row = input()
    #Save all rows with pieces
    if i % 2 != 0:
        board.append(row)

for r in range(len(board)):
    row = board[r]

    split_row = list(row)

    #Positions with possible pieces: 
    # 2, 6, 10, 14, 18, 22, 26, 30
    just_pieces = []
    for i in range(2, len(split_row), 4):
        just_pieces.append(split_row[i])
    

    print("pieces", just_pieces)

    for i in range(len(just_pieces)):
        if just_pieces[i].isalpha():
            if just_pieces[i].lower() != "p":
                out_string = just_pieces[i].upper() + column[i] + str(8-r)
            else:
                out_string = column[i] + str(8-r)

            if just_pieces[i].isupper():
                white.append(out_string)
            else:
                black.append(out_string)
    
#Order the strings
'''
Two pieces of same type in input:
White: smaller row number first in output
Black: larger row number first in output

Two pieces of same type in same row:
Smaller column letter first in output

Row-number: last digit in piece
Column-letter: second to last digit in piece
'''
def add_piece(piece, current_list, is_black):
    count = 0
    added = False
    if len(current_list) > 0:
        print("len(list) > 0", piece)
        if is_black:
            #larger row number first
            #Check for position
            for entry in current_list:
                print("piece =", piece, "piece[-1] =", piece[-1])
                print("entry =", entry, "entry[-1] =", entry[-1])
                if list(piece)[-1] > list(entry)[-1]:
                    print("int(piece[-1]) > int(entry[-1]) and count =", count)
                    current_list.insert(count, piece)
                    added = True
                    break
                elif int(piece[-1]) == int(entry[-1]):
                    #Check letter
                    if piece[-2] < entry[-2]:
                        current_list.insert(count, piece)
                        added = True
                        break
                count += 1
            if added == False:
                current_list.append(piece)
        else:
            #smaller row number first
            #Check for position
            for entry in current_list:
                if int(piece[-1]) < int(entry[-1]):
                    current_list.insert(count, piece)
                    added = True
                    break
                elif int(piece[-1]) == int(entry[-1]):
                    #Check letter
                    if piece[-2] < entry[-2]:
                        current_list.insert(count, piece)
                        added = True
                        break
                count += 1
            if added == False:
                current_list.append(piece)
    else:
        current_list.append(piece)
    
    return current_list
                

def sort_list(colour_list, is_black, out_list):
    kings = []
    queens = []
    rooks = []
    bishops = []
    knights = []
    pawns = []

    for piece in colour_list:
        if len(piece) == 2:
            add_piece(piece, pawns, is_black)
        else:
            if piece[0].lower() == "k":
                add_piece(piece, kings, is_black)
            elif piece[0].lower() == "q":
                add_piece(piece, queens, is_black)
            elif piece[0].lower() == "r":
                add_piece(piece, rooks, is_black)
            elif piece[0].lower() == "b":
                add_piece(piece, bishops, is_black)
            elif piece[0].lower() == "n":
                add_piece(piece, knights, is_black)

    out_list = kings + queens + rooks + bishops + knights + pawns

    return out_list
            
            

is_black = True
black_out = sort_list(black, is_black, black_out)

is_black = False
white_out = sort_list(white, is_black, white_out)

white_string = ",".join(white_out)
black_string = ",".join(black_out)

print("White: ", white)
print("Black: ", black)
print("\n")
print("White:", white_string)
print("Black:", black_string)