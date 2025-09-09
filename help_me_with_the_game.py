'''
Task:
Read picture of chessboard position and print in chess notation

Input:
Consists of an ASCII-art picture of a chessboard with chess 
pieces on positions described by the input. The pieces of 
the white player are shown in upper-case, while the black
player's pieces are lower-case.

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
of the piece in the standard chess notation – a lower-case 
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