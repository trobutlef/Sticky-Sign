import pygame as pg 
import thorpy
from StickyJump import *
from Learn import *
from Rules import *
from Settings import *

def init_game():
    currentState = None
    print(currentState)
    g = StickyJump(currentState, True)
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()
    __name__ = "__main__"
    background = thorpy.load_image("../pictures/Background1.png")
    e_bckgr = thorpy.Background.make(image=background, elements=elements)
    thorpy.store(e_bckgr)
    m=thorpy.Menu(e_bckgr)
    m.play()

def init_game2():
    currentState = None
    print(currentState)
    g = Learn()
    __name__ == "__main__"
    background = thorpy.load_image("../pictures/Background1.png")
    sticky_menu = thorpy.Background.make(image=background, elements=elements)
    thorpy.store(sticky_menu)
    m=thorpy.Menu(sticky_menu)
    m.play()

def init_game3():
    currentState = None
    print(currentState)
    g = Rules()
    __name__ == "__main__"
    background = thorpy.load_image("../pictures/Background1.png")
    sticky_menu = thorpy.Background.make(image=background, elements=elements)
    thorpy.store(sticky_menu)
    m=thorpy.Menu(sticky_menu)
    m.play()

if __name__ == "__main__":
    app = thorpy.Application((WIDTH,HEIGHT))
    thorpy.set_theme("human")
    screen = thorpy.get_screen()
    def play():
        print("playing")
    def calibrate():
        print("calibrating")

    sticky_logo = thorpy.Image.make(thorpy.load_image("../pictures/StickyLogo.png"))
    sticky_jump_image = "../pictures/JumpSmall.png"
    sticky_jump_image_hover = "../pictures/Jump.png"
    sticky_learn_image = "../pictures/LearnSmall.png"
    sticky_learn_image_hover = "../pictures/Learn.png"
    sticky_rules_image = "../pictures/RulesSmall.png"
    sticky_rules_image_hover = "../pictures/Rules.png"
    jump_button = thorpy.make_image_button(sticky_jump_image,sticky_jump_image_hover,sticky_jump_image_hover)
    jump_button.user_func = init_game
    learn_button= thorpy.make_image_button(sticky_learn_image,sticky_learn_image_hover,sticky_learn_image_hover)
    learn_button.user_func = init_game2
    rules_button = thorpy.make_image_button(sticky_rules_image,sticky_rules_image_hover,sticky_rules_image_hover)
    rules_button.user_func = init_game3
    elements = [sticky_logo, jump_button, learn_button, rules_button]
    background = thorpy.load_image("../pictures/Background1.png")
    sticky_menu = thorpy.Background.make(image=background, elements=elements)
    thorpy.store(sticky_menu)
    m=thorpy.Menu(sticky_menu)
    m.play()
    app.quit()
