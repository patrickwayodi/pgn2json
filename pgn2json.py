import chess.pgn
import json


# load a pgn file
pgn = open("Mukabi_vs_Anand_1988.pgn")


# read the game
game = chess.pgn.read_game(pgn)

# To convert the moves to standard algebraic notation, the position is needed for
# context, so we additionally make all the moves on a board
# https://stackoverflow.com/questions/63517471/printing-individual-moves-with-the-python-chess-library
board = game.board()


# convert the plies into a dictionary
plies = []

for ply in game.mainline_moves():
    
    # print(board.san(ply))

    plies.append(board.san(ply))

    board.push(ply)

print(plies)


# plies_dict = json.loads(plies)

keys = []
index = 1

for ply in plies:

    key = "p" + str(index)

    keys.append(key)

    index = index + 1


print(keys)


# https://stackoverflow.com/a/70322948/2247072
plies_dict = dict(zip(keys, plies))

print(plies_dict)


with open("game.json", "w") as outfile:
    json.dump(plies_dict, outfile, indent=4)

