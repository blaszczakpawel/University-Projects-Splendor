import tkinter as tk

import models.game.game as game

def main():
    game_to_play = game.Game()
    game_to_play.run()
    tk.mainloop()

if __name__ == "__main__":
    main()