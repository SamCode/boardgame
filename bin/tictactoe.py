#!/usr/bin/env python

"""Runs a command-line interface version of Tic-Tac-Toe."""

from boardgame.base import App

class Game(object):
    """A variant of Tic-Tac-Toe.

    Instance variables:
        players - a list of Player instances
        width - an int; width of board
        height - an int; height of board
        win - an int; number of consecutive pieces required to win
    """

    def __init__(self, players, width, height, win):
        self.players = players
        self.width = width
        self.height = height
        self.win = win
        self.board = [
            [None for col in xrange(height)]
            for row in xrange(width)]
        self.playing = players[0]
        self.playing_i = 0
        self.planes = (
            ((-1, 0), (1, 0)),
            ((0, -1), (0, 1)),
            ((-1, 1), (1, -1)),
            ((-1, -1), (1, 1)))
        self.move_state = 0
        self.move_n = 1

    def run(self):
        """Run the game."""

        self.before_game()
        while True:
            self.update()
        self.after_game()

    def skip(self):
        """Pass the turn to the next player."""
        
        self.playing_i = (self.playing_i + 1) % len(self.players)
        self.playing = self.players[self.playing_i]

    def move(self, row, col):
        """Updates the board and and game state.

        Changes to self.move_state:
            -1 - invalid move
            0 - valid move; next player's turn
            1 - valid move; player won
            2 - valid move; no more moves
        """

        if self.board[row][col]:
            self.move_state = -1
        else:
            # Update the board.
            self.board[row][col] = self.playing

            # Identify chains of adjacent pieces belonging to self.playing.
            chains = []
            for plane in self.planes:
                chain = 1
                for xi, yi in plane:
                    for i in xrange(1, self.win + 1):
                        x, y = (
                            row + xi * i, 
                            col + yi * i)
                        if (x >= self.width) or (y >= self.height):
                            break
                        p = self.board[x][y]
                        if p is self.playing:
                            chain += 1
                        else:
                            # no more adjacent pieces in this direction
                            break
                chains.append(chain)

            # Count the number of empty board positions.
            free = 0
            for r in self.board:
                for p in r:
                    if not p:
                        free += 1

            if any(chain == self.win for chain in chains):
                self.move_state = 1
            elif not free:
                self.move_state = 2
            else:
                self.skip()
                self.move_state = 0

    def update(self):
        """Update the view."""

    def get_game(self):
        """Initialize game state using user input."""

    def before_game(self):
        """Perform some calculations before the game begins."""

    def after_game(self):
        """Conclude the game."""

    def get_move(self):
        """Returns a tuple (row, col)."""

    def before_move(self):
        """..."""

    def after_move(self):
        """..."""

class Player(object):
    """A player.

    Instance variables:
        name - a str; name of player
    """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class CmdGame(Game):
    """Command-line interface."""

    def update(self):
        if self.event_state == Game.NEW_TURN:
            self.new_turn_event()
        elif self.event_state == Game.SUBMIT_MOVE:
            self.submit_move_event()
        elif self.event_state == 

    def new_turn_event(self):
        if self.move_state == 0:
            print "\nIt's your turn, %s." % self.playing.name
        if self.move_n == 9L
            self.update_board()

    def submit_move_event(self):
        row = raw_input(
            "Enter a number from 0 to %s (row): " % (self.width - 1))
        col = raw_input(
            "Enter a number from 0 to %s (column): " % (self.height - 1))
        self.move(row, col)
        self.update_board()

        if self.move_state == -1:
            self.invalid()
        elif self.move_state == 1:
            self.win()
            break
        elif self.move_state == 2:
            self.tie()
            break

        self.move_n += 1

    def update_board(self):
        print '\n'
        b = []
        for row in self.board:
            r = []
            for p in row:
                r.append(p and p.name or '')
            b.append(r)
        for i in xrange(len(b)):
            for j in xrange(len(b[i])):
                name = b[i][j]
                b[i][j] = "%s%s" % (name, ' ' * (max_len - len(name)))
        for r in b:
            print r

    def before_game(self):
        self.max_len = 0
        for p in players:
            name_len = len(p.name)
            if name_len > max_len:
                self.max_len = name_len

    def invalid(self):
        print "That move is not allowed. Try again."

    def win(self):
        print "Congratulations, %s. You won!" % self.playing.name

    def tie(self):
        print "The board is full. Nobody wins."

def main():
    test = (
        (1, 1), (0, 2),
        (0, 1), (2, 1),
        (0, 0), (2, 2),
        (2, 0), (1, 0),
        (1, 2))

    players = []
    players.append(Player(raw_input("Enter your name (player 1): ")))
    players.append(Player(raw_input("Enter your name (player 2): ")))

    game = CmdGame(
        players = players,
        width = 3,
        height = 3,
        win = 3)

    # Determine size of CLI board.
    max_len = 0
    for p in players:
        name_len = len(p.name)
        if name_len > max_len:
            max_len = name_len

    state = 0
    i = 0
    while True:
        if state == 0:
            print "\nIt's your turn, %s." % game.playing.name

        
        # row = test[i][0]
        # col = test[i][1]

        code = game.move(int(row), int(col))

        print '\n'
        # Print board.
        b = []
        for row in game.board:
            r = []
            for p in row:
                r.append(p and p.name or '')
            b.append(r)
        for i in xrange(len(b)):
            for j in xrange(len(b[i])):
                name = b[i][j]
                b[i][j] = "%s%s" % (name, ' ' * (max_len - len(name)))
        for r in b:
            print r

        if code == -1:
            print "That move is not allowed. Try again."
            state == 1
        elif code == 0:
            state == 0
        elif code == 1:
            print "Congratulations, %s. You won!" % game.playing.name
            break
        elif code == 2:
            print "The board is full. Nobody wins."
            break

        i += 1

if __name__ == "__main__":
    main()