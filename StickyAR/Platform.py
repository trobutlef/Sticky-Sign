import pygame as pg 
import thorpy
from StickyJump import *
# from stickys import updateSticky, clearSticky, calibrate, uncalibrate
from settings import *

# pg.init()
# pg.key.set_repeat(300, 30)
# screen = pg.display.set_mode((WIDTH,HEIGHT))
# screen.fill((255,255,255))

# pg.display.flip()

# #THORPY ELEMENTS
# # title_image = thorpy.make_image("n")
# quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
# sticky_jump_button = thorpy.make_button("StickyJump", func=launch_game) # < -- eventually abstract more
# calibrate_button = thorpy.make_button("Calibrate", func=print("calibrating")) # <-- zach add calibration here

# # box = thorpy.Box(elements=[sticky_jump_button,calibrate_button,quit_button])

# #we regroup all elements on a menu, even if we do not launch the menu
# e_background = thorpy.Background.make(elements=[sticky_jump_button,calibrate_button,quit_button])
# thorpy.store(e_background)
# m = thorpy.Menu(e_background)
# m.play()
# app.quit()
# #important : set the screen as surface for all elements
# for element in menu.get_population():
#     element.surface = screen

# #use the elements normally...
# box.set_topleft((WIDTH // 2, HEIGHT // 2))
# box.blit()
# box.update()

# playing_game = True
# while playing_game:
#     clock.tick(1)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             playing_game = False
#             break
#         menu.react(event) #the menu automatically integrate your elements

# pg.quit()

def init_game():
    #currentState = updateSticky()
    currentState = None
    print("attempt at retrieving currentState")
    print(currentState)
    print("launching game")
    g = StickyJump(currentState)
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

    logo = thorpy.Image.make(thorpy.load_image("Logo.png"))
    sticky_jump_image = "StickyJump.png"
    sticky_jump_image_hover = "StickyJumpHover.png"
    sticky_jam_image = "StickyJam.png"
    reset_image = "StickyReset.png"
    quit_image = "Credits.png"
    quit_image_hover = "CreditsHover.png"
    e_play = thorpy.make_image_button(sticky_jump_image,sticky_jump_image_hover,sticky_jump_image_hover)
    e_play.user_func = init_game
    e_play_2 = thorpy.make_image_button(sticky_jam_image,sticky_jam_image,sticky_jam_image)
    e_quit = thorpy.make_image_button(quit_image,quit_image_hover,quit_image_hover)
    e_quit.user_func = thorpy.functions.quit_menu_func
    elements = [logo, e_play, e_play_2, e_quit]
    background = thorpy.load_image("white.png")
    e_bckgr = thorpy.Background.make(image=background, elements=elements)
    thorpy.store(e_bckgr)
    m=thorpy.Menu(e_bckgr)
    m.play()
    app.quit()