import tkinter as tk

from models.game import game

def main():
    game_to_play = game.Game()
    game_to_play.run()
    tk.mainloop()

if __name__ == "__main__":
    main()