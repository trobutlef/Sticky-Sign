import pygame as pg 
import thorpy
from StickyJump import *
from Learn import *
from Settings import *

def init_game():
    currentState = None
    print("attempt at retrieving currentState")
    print(currentState)
    print("launching game")
    g = StickyJump(currentState, True)
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

def init_game2():
    currentState = None
    print("attempt at retrieving currentState")
    print(currentState)
    print("launching game")
    g = Learn(currentState, True)
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

if __name__ == "__main__":
    app = thorpy.Application((WIDTH,HEIGHT))
    thorpy.set_theme("human")
    screen = thorpy.get_screen()
    def play():
        print("playing")
    def calibrate():
        print("calibrating")

    logo = thorpy.Image.make(thorpy.load_image("../pictures/Logo.png"))
    sticky_jump_image = "../pictures/Jump.png"
    sticky_jump_image_hover = "../pictures/Jump.png"
    sticky_jam_image = "../pictures/Learn.png"
    reset_image = "../pictures/Reset.png"
    quit_image = "../pictures/Rules.png"
    quit_image_hover = "../pictures/Rules.png"
    e_play = thorpy.make_image_button(sticky_jump_image,sticky_jump_image_hover,sticky_jump_image_hover)
    e_play.user_func = init_game
    e_play_2 = thorpy.make_image_button(sticky_jam_image,sticky_jam_image,sticky_jam_image)
    e_play_2.user_func = init_game2
    e_quit = thorpy.make_image_button(quit_image,quit_image_hover,quit_image_hover)
    e_quit.user_func = thorpy.functions.quit_menu_func
    elements = [logo, e_play, e_play_2, e_quit]
    background = thorpy.load_image("../pictures/white.png")
    e_bckgr = thorpy.Background.make(image=background, elements=elements)
    thorpy.store(e_bckgr)
    m=thorpy.Menu(e_bckgr)
    m.play()
    app.quit()
