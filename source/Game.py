
# Virtual Date! 
# Copyright (C) 2022 QuetzalcoutlDev

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame, sys, lenpy
from source import config, textbox, screens, screenshot_f, Splash_screen, MainMenu, conversationSelector, con_themes

from source.dialog_box import dialog
from source.ui_text import bye_dialog

class Game(object):

    """
    Bienvenido, está es la clase del juego, está permite el tener el Splashscreen y el menú principal
    y el mismo juego en si.

    """
    
    def __init__(self):
        
        self.play_music_on = False

        config.current_screen = "splash"
        self.in_game = False

        self.white_img = pygame.image.load(f"{config.images_dir}/white.png").convert()
        self.white_img_alpha_value = 255

    def process_events(self):

        # Procesar los eventos

        # Si no se está en el juego en sí...

        if not config.in_game:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    # pygame.quit()
                    # config.data_manager.Save_game_data([config.default_data], ["tojiko"])
                    # sys.exit()

                    return True

            return False

        elif config.in_game:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    dialog(bye_dialog)

    def draw_screen(self):

        # Está función permite el dibujado de las pantallas del juego
        # que en sí es la más critica e importante de todo el juego

        if config.current_screen == "splash":

            self.splash()

            # print(config.firstrun)

            if Splash_screen.splashscreen.number_img == 3:

                if config.firstrun:

                    config.current_screen = "MainMenu"

                elif not config.firstrun:

                    #self.in_game = True
                    config.current_screen = "Game"

        elif config.current_screen == "MainMenu" or config.current_screen == "ConfigScreenMain":

            self.main_menu()
        
        elif config.current_screen == "Game" or config.current_screen == "ConfigScreen" or config.current_screen == "musicSelector" or config.current_screen == "conversationselector" or config.current_screen == "con_themes_section" or config.current_screen == "i_feel_section" or config.current_screen ==  "make_question_section" or config.current_screen == "make_compliments_section" or config.current_screen == "text_window" or config.current_screen == "configCamera" or config.current_screen == "introGame":

            config.in_game = True

            if self.play_music_on == False:

                lenpy.ui.UIaction(f"play:{config.music_dir}/{config.game_music_default}")
                self.play_music_on = True

            ###################################
            ###################################
            ###################################
            ###################################

            # cambiar valor alpha

            self.white_img.set_alpha(self.white_img_alpha_value)

            # efecto de transición alpha entrada

            if self.white_img_alpha_value > 0 and textbox.not_intro:

                self.white_img_alpha_value -= 10
                config.current_screen = "introGame"

            elif self.white_img_alpha_value <= 0 and textbox.not_intro:

                config.current_screen = "Game"
                self.white_img_alpha_value = 0
                textbox.not_intro = False

            ###################################
            ###################################
            ###################################
            ###################################

            # Este es el juego en si :)

            surf = pygame.transform.scale(config.canvas, config.canvas_size)
            config.screen.fill(config.BLACK)
            config.screen.blit(surf, config.canvas_pos)

            config.canvas.fill(config.GRAY)
            config.bg.draw(config.bg_x, config.bg_y, config.set_antialiasing)
            config.tojiko.draw([config.tojiko_bg_x, config.tojiko_bg_y], config.set_antialiasing)

            # Dibujar las pantallas
            screens.draw_screens()

            # Dibuja la caja de texto
            if not textbox.not_intro:
                textbox.textbox_show_hide()

            if not textbox.not_intro and config.firstrun and config.welcome_again_no_more:

                config.textbox_visibility = True
                config.welcome_again_no_more = False
                conversationSelector.conversationselector.call_textbox(con_themes.welcome_to_virtual_date, config.textbox_visibility)

            elif not textbox.not_intro and config.welcome_again_text and config.welcome_again_no_more:

                config.textbox_visibility = True
                config.welcome_again_no_more = False
                conversationSelector.conversationselector.call_textbox(con_themes.welcome_again, config.textbox_visibility)

            # Otras cosas
            config.notify_counter()
            config.notify.notify(config.notify_message, config.notify_visibility)
            config.display_fps(config.show_fps_counter)

            # Blanco
            config.canvas.blit(self.white_img, [0, 0])

        # Actualiza toda la pantalla
        pygame.display.flip()

    def main_menu(self):

        """
        Cargar el menú principal si es requerido
        """

        MainMenu.m_menu.Screen()

    def splash(self):

        """
        El splash es la primera pantalla que se ve durante el inicio del juego

        """

        # Dibuja la pantalla de Splash
        Splash_screen.splashscreen.Screen()

        # Actualiza los elementos en este
        Splash_screen.splashscreen.update() 