import pygame

from buffalo import utils

from main_menu import MainMenu

def main():
    
    while not utils.end:
        utils.scene.logic()
        utils.scene.update()
        utils.scene.render()
        utils.delta = utils.clock.tick( utils.FRAMES_PER_SECOND )

if __name__ == "__main__":
    
    if not utils.init(
            caption="Mganga",
    ):
        print("buffalo.utils failed to initialize")
        pygame.quit()
        exit()
    
    utils.set_scene( MainMenu() )
    
    main()
    
    pygame.quit()
