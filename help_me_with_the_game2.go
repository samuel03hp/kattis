package main

import (
	"fmt"
	"strconv"
	"strings"
)

var (
	board  = []string{}
	white  = []string{}
	black  = []string{}
	column = [...]string{"a", "b", "c", "d", "e", "f", "g", "h"}

	white_out = []string{}
	black_out = []string{}

	is_black bool

	white_string string
	black_string string
)

func isUpper(s string) bool {
	return s == strings.ToUpper(s)
}

func add_piece(piece string, current_list []string, is_black bool) (new_current_list []string) {
	new_current_list = current_list
	var count int = 0
	var added bool = false

	if len(new_current_list) > 0 {
		if is_black {
			//larger row number first
			for _, entry := range new_current_list {
				// last character as a byte
				piece_last := piece[len(piece)-1]
				entry_last := entry[len(entry)-1]

				// convert from ASCII to int
				piece_num := int(piece_last - '0')
				entry_num := int(entry_last - '0')

				if piece_num > entry_num {
					new_current_list = append(new_current_list[:count], append([]string{piece}, new_current_list[count:]...)...)
					added = true
					break
				} else if piece_num == entry_num {
					piece_letter := piece[len(piece)-2]
					entry_letter := entry[len(entry)-2]
					if piece_letter < entry_letter {
						new_current_list = append(new_current_list[:count], append([]string{piece}, new_current_list[count:]...)...)
						added = true
						break
					}
				}
				count += 1
			}
			if !added {
				new_current_list = append(new_current_list, piece)
			}
		} else {
			//smaller row number first
			for _, entry := range new_current_list {
				// last character as a byte
				piece_last := piece[len(piece)-1]
				entry_last := entry[len(entry)-1]

				// convert from ASCII to int
				piece_num := int(piece_last - '0')
				entry_num := int(entry_last - '0')

				if piece_num < entry_num {
					new_current_list = append(new_current_list[:count], append([]string{piece}, new_current_list[count:]...)...)
					added = true
					break
				} else if piece_num == entry_num {
					piece_letter := piece[len(piece)-2]
					entry_letter := entry[len(entry)-2]
					if piece_letter < entry_letter {
						new_current_list = append(new_current_list[:count], append([]string{piece}, new_current_list[count:]...)...)
						added = true
						break
					}
				}
				count += 1
			}
			if !added {
				new_current_list = append(new_current_list, piece)
			}

		}
	} else {
		new_current_list = append(new_current_list, piece)
	}

	return new_current_list
}

func sort_list(colour_list []string, is_black bool) (out_list []string) {
	var (
		kings   = []string{}
		queens  = []string{}
		rooks   = []string{}
		bishops = []string{}
		knights = []string{}
		pawns   = []string{}
	)

	for _, piece := range colour_list {
		if len(piece) == 2 {
			//pawn
			pawns = add_piece(piece, pawns, is_black)
		} else {
			first := string(piece[0])
			first_lower := strings.ToLower(first)
			switch first_lower {
			case "k":
				kings = add_piece(piece, kings, is_black)
			case "q":
				queens = add_piece(piece, queens, is_black)
			case "r":
				rooks = add_piece(piece, rooks, is_black)
			case "b":
				bishops = add_piece(piece, bishops, is_black)
			case "n":
				knights = add_piece(piece, knights, is_black)
			}
		}
	}

	all := [][]string{kings, queens, rooks, bishops, knights, pawns}

	for _, l := range all {
		out_list = append(out_list, l...)
	}

	return out_list
}

func main() {
	var row string
	var out_string string
	for i := range 17 {
		fmt.Scanln(&row)

		if i%2 != 0 {
			board = append(board, row)
		}
	}
	for r := range len(board) {
		row = board[r]

		split_row := make([]string, len(row))

		for i, j := range row {
			split_row[i] = string(j)
		}

		var just_pieces = []string{}
		for i := 2; i < len(split_row); i += 4 {
			just_pieces = append(just_pieces, split_row[i])
		}

		for i := range len(just_pieces) {
			if strings.ToLower(just_pieces[i]) != "p" {
				out_string = strings.ToUpper(just_pieces[i]) + column[i] + strconv.Itoa(8-r)
			} else {
				out_string = column[i] + strconv.Itoa(8-r)
			}

			if isUpper(just_pieces[i]) {
				white = append(white, out_string)
			} else {
				black = append(black, out_string)
			}
		}
	}

	is_black = true
	black_out = sort_list(black, is_black)

	is_black = false
	white_out = sort_list(white, is_black)

	black_string = strings.Join([]string(black_out), ",")
	white_string = strings.Join([]string(white_out), ",")

	fmt.Println("White:", white_string)
	fmt.Println("Black:", black_string)
}
