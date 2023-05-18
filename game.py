class Player:
    def __init__(self,c,n):
        self.char = c
        self.num = n
        self.row = None
        self.col = None

class TicTacToe:
   
    # Function to handle printing the Grid
    def print_grid(self):
        print("  ['1', '2', '3']")
        for i in range(0,3):
            print (str(i+1) + ' ' + str(self.grid[i]))

    # Function to handle updating the Grid
    def update_grid(self,player = Player):
        for r in range(0,3):
            if r == (player.row -1):
                 for c in range(0,3):
                    if c == (player.col -1):
                        self.grid[r][c] = player.char
        self.print_grid()

    def game_status(self,winner):
        self.game_over = False 
        counter=0
        for i in range(0,3):
            if self.grid[i][0] == self.grid[i][1] and self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != ' ':
                self.game_over = True 
                print("Winner is Player {}".format(winner.num))
                return
            elif self.grid[0][i] == self.grid[1][i] and self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != ' ':
                self.game_over = True
                print("Winner is Player {}".format(winner.num))
                return
            elif self.grid[0][0] == self.grid[1][1] and self.grid[1][1] == self.grid[2][2] and self.grid[i][0] != ' ':
                self.game_over = True           
                print("Winner is Player {}".format(winner.num))
                return
            else: 
                for j in range(0,3):
                    if self.grid[i][j] == ' ': 
                        counter +=1
        if counter == 0:
            self.game_over = True
            print("It is a tie.")

    def game_play(self):
        i = 0
        while  self.game_over == False:
            if i%2==0: p = self.p1
            else: p = self.p2
            try:
                p.row = int(input("Player {}'s turn: \ninput Row: ".format(p.num)))
                p.col = int(input("input Column: "))
            except: print("error")
            if p.row == None or p.col == None: print("Please try again: the location does not exist")
            elif p.row>3 or p.col>3: print("Please try again: the location does not exist")
            elif self.grid[p.row-1][p.col-1] == ' ':
                self.update_grid(p)
                i+=1
                self.game_status(p)
            else: print("Please try again: the location is already occupied")



    def __init__(self):
        self.grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        print("Welcome to Tic Tac Toe! \nTo use the game identify your selection of the location as row,column. \nThe game will detect if you are Player 1 (X) or Player 2 (O)")  
        self.p1 = Player('X',1)
        self.p2 = Player('O',2)
        self.print_grid()
        self.game_over = False 
        self.game_play()

TicTacToe()

